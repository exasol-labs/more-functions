--| CREATE OR REPLACE LUA SCALAR SCRIPT bin (val DECIMAL(36,0))
--| RETURNS VARCHAR(128) AS
local ZERO = decimal(0, 36, 0)
local TWO_TO_32 = decimal("4294967296", 36, 0)
local MAX_UNSIGNED_64 = decimal("18446744073709551615", 36, 0)
local TWO_TO_64 = decimal("18446744073709551616", 36, 0)
local MIN_NEGATIVE_WRAP = ZERO - MAX_UNSIGNED_64

local function normalize_unsigned_64(value)
    if value > MAX_UNSIGNED_64 then
        return MAX_UNSIGNED_64
    end

    if value < MIN_NEGATIVE_WRAP then
        return MAX_UNSIGNED_64
    end

    if value < ZERO then
        return TWO_TO_64 + value
    end

    return value
end

local function truncate_fraction(value)
    local text = tostring(value)
    if text:find("[%.eE]") then
        local number = tonumber(value)
        if number ~= nil then
            if number >= 0 then
                return math.floor(number)
            end
            return math.ceil(number)
        end
    end
    return value
end

local function to_binary_string_32(value)
    if value == 0 then
        return "0"
    end

    local digits = {}
    local current = value
    while current > 0 do
        local bit = current & 1
        digits[#digits + 1] = (bit == 0) and "0" or "1"
        current = current >> 1
    end

    local result = {}
    for i = #digits, 1, -1 do
        result[#result + 1] = digits[i]
    end
    return table.concat(result)
end

local function to_binary_string(value)
    if value == ZERO then
        return "0"
    end

    local lower_32_decimal = value % TWO_TO_32
    local lower_32 = tonumber(tostring(lower_32_decimal))
    local upper_32 = tonumber(tostring((value - lower_32_decimal) / TWO_TO_32))

    if upper_32 == 0 then
        return to_binary_string_32(lower_32)
    end

    local lower_bits = to_binary_string_32(lower_32)
    local upper_bits = to_binary_string_32(upper_32)
    return upper_bits .. string.rep("0", 32 - #lower_bits) .. lower_bits
end

function run(ctx)
    -- [impl -> dsn~bin-null~1]
    if ctx.val == null then
        return null
    end

    -- [impl -> dsn~bin-integer-literal~1]
    -- [impl -> dsn~bin-exact-numeric-integer~1]
    -- [impl -> dsn~bin-floating-point-integer~1]
    -- [impl -> dsn~bin-ignore-higher-bits~1]
    return to_binary_string(normalize_unsigned_64(truncate_fraction(ctx.val)))
end
