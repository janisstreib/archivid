local autoloop_duration = .5


local was_loop = mp.get_property_native("loop-file")

function set_loop()
    mp.command('set hidetimeout 0')
    local duration = mp.get_property_native("duration")
    if duration ~= nil then
        if duration  < autoloop_duration + 0.001 then
            mp.set_property_native("loop-file", was_loop)
        else
            mp.command("set loop-file 5")
        end
    else
        mp.set_property_native("loop-file", was_loop)
    end
end

mp.register_event("file-loaded", set_loop)
