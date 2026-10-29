"""原本の個体仮想アドレスと走査終端を、通常/拡張で共用する。"""
import re


def adapt_actor_pool(text):
    def address(match):
        value = int(match[0], 16)
        if 0xC804 < value < 0xCBF0:
            return f'(actorStride+0x{value - 0xC804:x})'
        if 0x84080 <= value < 0x9D088:
            offset = value - 0x84080
            return f'(actorBase+{offset // 0xC804}*actorStride+0x{offset % 0xC804:x})'
        return match[0]

    text = re.sub(r'\b0x[0-9a-fA-F]+\b', address, text)
    text = text.replace('0xc804', 'actorStride')
    text = re.sub(r'(\} while \([^;\n]*?)!= 0x33', r'\1!= ctx.limit()', text)
    text = re.sub(r'(uVar(?:8|12|32)) != ctx.limit\(\)', r'\1 != uint64_t(ctx.limit())', text)
    text = text.replace('iVar9 + 1U != ctx.limit()', 'iVar9 + 1U != uint32_t(ctx.limit())')
    text = text.replace('uVar32 < 0x32', 'uVar32 < uint32_t(ctx.limit()-1)')
    text = text.replace('lVar65 = -0x32;', 'lVar65 = 1-ctx.limit();')
    text = text.replace('(int32_t)lVar65 + 0x33', '(int32_t)lVar65 + ctx.limit()')
    text = text.replace('(uint64_t)(uVar5 | 0x80000)', '(actorBase+uVar5-0x4080)')
    text = text.replace('ctx.clock->forms[0][param_2]', 'actorForm(ctx.clock,0,param_2)')
    text = text.replace('ctx.clock->kill_orb[param_2]', 'actorKillOrb(ctx.clock,param_2)')
    return text
