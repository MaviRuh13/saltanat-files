quest baska_bayrak_engelle begin
	state start begin
		when login begin
			if pc.get_map_index() == 44 and pc.get_empire() == 1 and not pc.is_gm() then
			pc.warp(469300,964200)
			elseif pc.get_map_index() == 44 and pc.get_empire() == 2 and not pc.is_gm() then
			pc.warp(55700,157900)
			elseif pc.get_map_index() == 24 and pc.get_empire() == 1 and not pc.is_gm() then
			pc.warp(469300,964200)
			elseif pc.get_map_index() == 24 and pc.get_empire() == 3 and not pc.is_gm() then
			pc.warp(969600,278400)
			elseif pc.get_map_index() == 4 and pc.get_empire() == 2 and not pc.is_gm() then
			pc.warp(55700,157900)
			elseif pc.get_map_index() == 4 and pc.get_empire() == 3 and not pc.is_gm() then
			pc.warp(969600,278400)
			end
		end
	end
end