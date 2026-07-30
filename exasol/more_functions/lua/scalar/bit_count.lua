-- [impl -> dsn~bit-count-function~2]
-- [impl -> dsn~lua-function-source-header~1]
--| CREATE OR REPLACE LUA SCALAR SCRIPT bit_count (val DECIMAL(36,0))
--| RETURNS DECIMAL(2,0) AS
local ZERO = decimal(0, 36, 0)
local ONE = decimal(1, 36, 0)
local TWO_TO_32 = decimal("4294967296", 36, 0)
local MAX_UNSIGNED_64 = decimal("18446744073709551615", 36, 0)
local MIN_SIGNED_64 = decimal("-9223372036854775808", 36, 0)
local MAX_32 = 0xFFFFFFFF

local function count_set_bits_32(value)
    local current = value
    local count = 0
    while current ~= 0 do
        if (current & 1) ~= 0 then
            count = count + 1
        end
        current = current >> 1
    end
    return count
end

-- [impl -> dsn~bit-count-ignore-higher-bits~1]
local function count_lower_64_bits(value)
    if value > MAX_UNSIGNED_64 then
        return 64
    end
    if value < MIN_SIGNED_64 then
        return 1
    end

    local normalized = value
    local invert = normalized < ZERO
    if invert then
        -- Decimal userdata supports binary subtraction, but not unary negation.
        normalized = ZERO - (normalized + ONE)
    end

    local lower_32_decimal = normalized % TWO_TO_32
    local lower_32 = tonumber(tostring(lower_32_decimal))
    normalized = (normalized - lower_32_decimal) / TWO_TO_32
    local upper_32 = tonumber(tostring(normalized % TWO_TO_32))
    if invert then
        lower_32 = MAX_32 - lower_32
        upper_32 = MAX_32 - upper_32
    end
    return count_set_bits_32(lower_32) + count_set_bits_32(upper_32)
end

function run(ctx)
    -- [impl -> dsn~bit-count-null~1]
    if ctx.val == null then
        return null
    end
    -- [impl -> dsn~bit-count-integer-literal~1]
    -- [impl -> dsn~bit-count-exact-numeric-integer~1]
    -- [impl -> dsn~bit-count-floating-point-integer~1]
    return decimal(count_lower_64_bits(ctx.val), 2, 0)
end
