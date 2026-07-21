-- [impl -> dsn~bit-count-function~1]
CREATE OR REPLACE LUA SCALAR SCRIPT bit_count (val DECIMAL(36,0))
RETURNS DECIMAL(36,0) AS
local ZERO = decimal(0, 36, 0)
local ONE = decimal(1, 36, 0)
local TWO_TO_32 = decimal("4294967296", 36, 0)
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

local function split_unsigned_128_to_32(value)
    local normalized = value
    local invert = normalized < ZERO
    if invert then
        normalized = -(normalized + ONE)
    end

    local blocks = {}
    for index = 1, 4 do
        local block = normalized % TWO_TO_32
        local block_int = tonumber(tostring(block))
        if invert then
            block_int = MAX_32 - block_int
        end
        blocks[index] = block_int
        normalized = (normalized - block) / TWO_TO_32
    end
    return blocks
end

function run(ctx)
    -- [impl -> dsn~bit-count-null~1]
    if ctx.val == null then
        return null
    end
    -- [impl -> dsn~bit-count-integer-literal~1]
    -- [impl -> dsn~bit-count-exact-numeric-integer~1]
    -- [impl -> dsn~bit-count-floating-point-integer~1]
    local blocks = split_unsigned_128_to_32(ctx.val)
    local count = 0
    for index = 1, 4 do
        count = count + count_set_bits_32(blocks[index])
    end
    return decimal(count, 36, 0)
end
/
