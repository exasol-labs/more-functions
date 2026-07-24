package = "more-functions"
version = "0.1.0-1"
rockspec_format = "3.0"

source = {
   url = "git+https://github.com/exasol/more-functions.git"
}

description = {
   summary = "Lua development dependencies for more-functions",
   homepage = "https://github.com/exasol/more-functions",
   license = "MIT"
}

dependencies = {
   "luacheck == 1.2.0-1"
}

build = {
   type = "none"
}
