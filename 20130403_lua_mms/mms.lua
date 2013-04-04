local function escalar(v1, v2)
    local soma
    if #v1 == #v2 then
        soma = 0
        for i = 1, #v1 do
             soma = soma + v1[i]*v2[i]
        end
    end
    return soma
end

local function menor_escalar(v1, v2)
    table.sort(v1)
    table.sort(v2, function (a,b) return a > b end )
    return escalar(v1,v2)
end

return {
    escalar = escalar,
    menor_escalar = menor_escalar,

}
