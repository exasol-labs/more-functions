-- [impl -> dsn~bit-count-function~1]
CREATE OR REPLACE LUA SCALAR SCRIPT bit_count (value DECIMAL(36,0))
RETURNS DECIMAL(36,0) AS
local ZERO = decimal(0, 36, 0)
local ONE = decimal(1, 36, 0)
local TWO = decimal(2, 36, 0)
local TWO_TO_63 = TWO ^ 63
local TWO_TO_64 = TWO_TO_63 * TWO
local MIN_SIGNED_64 = -TWO_TO_63
local MAX_UNSIGNED_64 = TWO_TO_64 - ONE
local RANGE_ERROR = "BIT_COUNT only supports 64-bit integer values."

local function to_unsigned_64(value)
    if value < MIN_SIGNED_64 or value > MAX_UNSIGNED_64 then
        error(RANGE_ERROR)
    end

    if value < ZERO then
        return value + TWO_TO_64
    end

    return value
end

function run(ctx)
    -- [impl -> dsn~bit-count-null~1]
    if ctx.value == null then
        return null
    end

    local current = to_unsigned_64(ctx.value)
    local count = decimal(0, 36, 0)

    -- [impl -> dsn~bit-count-integer-literal~1]
    -- [impl -> dsn~bit-count-exact-numeric-integer~1]
    -- [impl -> dsn~bit-count-floating-point-integer~1]
    while current ~= ZERO do
        local remainder = current % TWO
        if remainder ~= ZERO then
            count:add(ONE)
        end
        current = (current - remainder) / TWO
    end

    return count
end
/
