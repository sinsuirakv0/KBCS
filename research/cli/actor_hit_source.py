"""命中本体のコンテナ・文字列を明示入力へ置換する。ゲーム分岐は保持する。"""
import re


def hit_source(source, clean, enemy):
    address = '006e79bc' if enemy else '006e4aec'
    text = clean(source(address))
    signature = text[:text.index('{')]
    start = text.index('  uVar5 = FUN_005bc1dc' if enemy else '  uVar19 = thunk_')
    text = text[start:]
    # 12属性のmapは、対象属性に基づく本能玉を解決した入力に置換する。
    start = text.index('  local_cc = ' if enemy else '    local_cc = ')
    end = text.index('FUN_0065f698(', start)
    end = text.index(';', end) + 1
    text = text[:start] + text[end:]
    text = text.replace('thunk_FUN_00a94484(1,param_4)', 'FUN_00a94484(1,param_4,param_3)')
    text = text.replace('thunk_FUN_00a94484(', 'FUN_00a94484(')
    text = text.replace('FUN_00a96a38(1,1,param_3)', 'FUN_00a96a38(1,param_3)')
    text = text.replace('auStack_e8', '0')
    # param.tsvの取得結果を入力にする。二重取得も同じ値を返す。
    for key, index in [('local_108', 0), ('local_120', 1), ('local_140', 1), ('local_160', 2), ('local_180', 2)]:
        if enemy:
            index = {'local_108': 0, 'local_120': 3, 'local_140': 3, 'local_160': 4, 'local_180': 4}[key]
        text = re.sub(r'FUN_009019f4\(param_1 \+ 0x14a0,&' + key + r',\w+\)', 'ctx.hit->parameters[' + str(index) + ']', text)
    if enemy:
        for key, index in [('local_120', 3), ('local_138', 3), ('local_150', 4), ('local_168', 4)]:
            text = re.sub(r'FUN_009019f4\(param_1 \+ 0x14a0,' + key + r',\w+\)', 'ctx.hit->parameters[' + str(index) + ']', text)
    # メタルキラーの予約と撃破寄与mapは戦闘所有者が保持する。
    if not enemy:
        start = text.index('          puVar28 = (undefined8 *)(param_1 + 0x84070);')
        end = text.index('          FUN_00a9d32c(1,param_4,1);', start)
        text = text[:start] + '          ctx.reserveMetal(param_4,param_18);\n' + text[end:]
        start = text.index('      __c = FUN_00a956f8')
        end = text.index('      FUN_00a9bbac(1,param_4,local_198);', start)
        text = text[:start] + '      ctx.creditHit(param_3,param_4);\n' + text[end:]
    # 文字列の解放だけを除く。空になったlabelはgotoの到達点として残す。
    text = re.sub(r' +if \(\(local_\w+(?:\[0\])? & 1\) != 0\) \{\n +operator_delete\([^;]+;\n +\}', '', text)
    text = re.sub(r' +FUN_0041b298\([^;]+;', '', text)
    text = re.sub(r' +FUN_0066ba4c\([^;]+;', '', text)
    text = re.sub(r'^ +[^;\n]*\b(?:local_(?:108|107|110|120|130|140|150|160|170|180)|uStack_\w+|cStack_\w+|s_battle_\w+)\b[^;]*;', '', text, flags=re.M)
    text = re.sub(r'^ +(?:uVar\d+) = (?:_DAT_|_UNK_|s_battle_|CONCAT)[^;]+;', '', text, flags=re.M)
    # ARM64のSMULHによる符号付き/100を明示する（掛算自体は64bit）。
    text = re.sub(r'lVar(25|17) = SUB168\(SEXT816\((.*?)\) \* SEXT816\(-0x5c28f5c28f5c28f5\),8\) \+\s*\2;\n +uVar(19|13) = \(lVar\1 >> 6\) - \(lVar\1 >> 0x3f\);', r'uVar\3 = (\2) / 100;', text, flags=re.S)
    text = re.sub(r'uVar14 = SUB168\(SEXT816\((.*?)\) \* SEXT816\(-0x5c28f5c28f5c28f5\),8\)\s*\+\s*\1;\n +iVar7 = FUN_0044abe4\(\(int\)\(uVar14 >> 6\) - \(int\)\(\(long\)uVar14 >> 0x3f\),1\);', r'iVar7 = FUN_0044abe4((\1) / 100,1);', text, flags=re.S)
    text = re.sub(r'^ +ctx.hit->parameters\[\d\];', '', text, flags=re.M)
    text = text.replace('LAB_006e8be0:', 'LAB_006e8be0:;')
    text = text.replace('bVar10 & local_198 != 0', 'bVar10 & (local_198 != 0)')
    text = text.replace('param_7 | uVar12 ^ 0xffffffff', 'param_7 | (uVar12 ^ 0xffffffff)')
    text = text.replace('DAT_002b29a0', '0x100000000ULL')
    text = text.replace('bVar4 & *(int *)(param_1 + 0x4dc) != -1', 'bVar4 & (*(int *)(param_1 + 0x4dc) != -1)')
    if enemy:
        text = text[:text.index('  if (*(long *)(lVar1 + 0x28)')] + '  return uVar5;\n}'
        locals_ = 'bool bVar2;byte bVar4;undefined4 uVar5,uVar6,uVar11;int iVar7,iVar8,iVar9,iVar10;uint uVar12;ulong uVar13,uVar14,uVar15;undefined8 uVar16;long lVar17;'
    else:
        text = text[:text.index('  if (*(long *)(lVar3 + 0x28)')] + '  return uVar11;\n}'
        locals_ = 'byte bVar10;undefined4 uVar11,uVar12,uVar18;int iVar13,iVar14,iVar15,iVar16;uint uVar17;ulong uVar19,uVar20,uVar29,local_198;long lVar25;'
    assert not any(token in text for token in ['operator_', 'Stack_', 'SUB', 's_battle_', 'FUN_009019f4', 'local_108', 'puVar', 'pwVar', 'tpidr']), text
    return signature + '{\n  ' + locals_ + '\n' + text
