require 'busted'

local mms = require 'mms'

describe('Test produto escalar', function()
    it('multiplica 2 vetores iguais', function()
        a = {1}
        b = {1}
        assert.are.equal(1, mms.escalar(a, b))
    end)
    
    it('multiplica 2 vetores diferentes', function()
        a = {1}
        b = {2}
        assert.are.equal(2, mms.escalar(a, b))
    end)
    
    it('multiplica 2 vetores iguais - o retorno', function()
        a = {2}
        b = {2}
        assert.are.equal(4, mms.escalar(a, b))
    end)

    it('multiplica 2 vetores iguais de tamanho 2', function()
        a = {2,2}
        b = {2,2}
        assert.are.equal(8, mms.escalar(a, b))
    end)

    it('multiplica 2 vetores de n valores', function()
        a = {2,2,2,2}
        b = {2,2,2,2}
        assert.are.equal(16, mms.escalar(a, b))
    end)
    
    it('retorna nil com tamanhos diferentes', function()
        a = {2,2}
        b = {2,2,2,2}
        assert.has.errors(function () assert(mms.escalar(a, b)) end)
    end)

end)

describe('Test menor produto escalar', function()
    it('multiplica 2 vetores conhecidos', function()
        a = {3,1,5}
        b = {8,2,3}
        assert.are.equal(27, mms.menor_escalar(a, b))
    end)
    
    it('multiplica 2 vetores conhecidos', function()
        a = {1,3,-5}
        b = {-2,4,1}
        assert.are.equal(-25, mms.menor_escalar(a, b))
    end)
    
    it('multiplica 2 vetores conhecidos', function()
        a = {1,2,3,4,5}
        b = {1,0,1,0,1}
        assert.are.equal(6, mms.menor_escalar(a, b))
    end)
end)
