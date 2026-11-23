# 005abeac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `005abeac`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ab/005abeac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0013.md#compare-4a3e0a83ff13698dd4d28a4894acbf8a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `005abeac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005ab/005abeac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0013.md#compare-06fc1fd2da353032296eff383e6db4db)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005abeac",
  "name": "FUN_005abeac",
  "size": 768,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aaef458c7f5e427e9e86cbb4dd55b898aa2b1c9ffa848bd4505a9b873d039697",
  "source_text_sha256": "aaef458c7f5e427e9e86cbb4dd55b898aa2b1c9ffa848bd4505a9b873d039697",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005abeac",
        "005ac1ab"
      ]
    ],
    "bytes_sha256": "eaf6b508c9bf1a6baab74bb98fb7450d0ac9059ae275641c1ed36ac168eb1925",
    "instruction_count": 192,
    "instruction_bytes": 768,
    "body_bytes": 768,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005a9c58](../005a9/005a9c58.md)
- [005ae770](../005ae/005ae770.md)

## 呼び出し先

- [005abb94](../005ab/005abb94.md)
- [005ac1ac](../005ac/005ac1ac.md)
- [00bdd940](../00bdd/00bdd940.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4528 bytes

~~~c

byte * FUN_005abeac(long param_1,byte *param_2,byte *param_3,long param_4)

{
  byte bVar1;
  ulong uVar2;
  int iVar3;
  uint uVar4;
  int iVar5;
  uint uVar6;
  int iVar7;
  
  if (param_2 == param_3) {
    return param_2;
  }
  bVar1 = *param_2;
  uVar2 = (ulong)bVar1;
  if (bVar1 < 0x72) {
    if (bVar1 < 0x66) {
      if (bVar1 == 0x30) {
        if (param_4 != 0) {
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,0);
          goto LAB_005ac194;
        }
        uVar2 = 0;
      }
      else {
        if (bVar1 == 99) {
          if ((param_2 + 1 != param_3) && (bVar1 = param_2[1], (byte)((bVar1 & 0xdf) + 0xbf) < 0x1a)
             ) {
            if (param_4 != 0) {
              _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4);
              return param_2 + 2;
            }
            FUN_005ac1ac(param_1,bVar1 & 0x1f);
            return param_2 + 2;
          }
          goto LAB_005ac1a8;
        }
        if (bVar1 == 0x5f) goto LAB_005ac1a8;
LAB_005ac168:
        if ((-1 < (char)bVar1) &&
           ((*(ulong *)(*(long *)(*(long *)(param_1 + 8) + 0x10) + uVar2 * 8) & 0x60) != 0))
        goto LAB_005ac1a8;
        if (param_4 != 0) {
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4);
          goto LAB_005ac194;
        }
      }
    }
    else if (bVar1 == 0x66) {
      if (param_4 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,0xc);
        goto LAB_005ac194;
      }
      uVar2 = 0xc;
    }
    else {
      if (bVar1 != 0x6e) goto LAB_005ac168;
      if (param_4 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,10);
        goto LAB_005ac194;
      }
      uVar2 = 10;
    }
  }
  else {
    if (0x74 < bVar1) {
      if (bVar1 == 0x75) {
        if (param_2 + 1 == param_3) goto LAB_005ac1a8;
        bVar1 = param_2[1];
        uVar4 = (uint)bVar1;
        iVar3 = 0xffd0;
        if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
          uVar4 = bVar1 | 0x20;
          if (5 < uVar4 - 0x61) goto LAB_005ac1a8;
          iVar3 = 0xffa9;
        }
        param_2 = param_2 + 2;
        if (param_2 == param_3) goto LAB_005ac1a8;
        bVar1 = *param_2;
        uVar6 = (uint)bVar1;
        iVar5 = 0xffd0;
        if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
          uVar6 = uVar6 | 0x20;
          if (5 < uVar6 - 0x61) goto LAB_005ac1a8;
          iVar5 = 0xffa9;
        }
        iVar3 = (iVar3 + uVar4) * 0x100 + (iVar5 + uVar6) * 0x10;
      }
      else {
        if (bVar1 == 0x76) {
          if (param_4 != 0) {
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,0xb);
            goto LAB_005ac194;
          }
          uVar2 = 0xb;
          goto LAB_005ac190;
        }
        if (bVar1 != 0x78) goto LAB_005ac168;
        iVar3 = 0;
      }
      if (param_2 + 1 != param_3) {
        bVar1 = param_2[1];
        uVar4 = (uint)bVar1;
        iVar5 = 0xffd0;
        if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
          uVar4 = uVar4 | 0x20;
          if (5 < uVar4 - 0x61) goto LAB_005ac1a8;
          iVar5 = 0xffa9;
        }
        if (param_2 + 2 != param_3) {
          bVar1 = param_2[2];
          uVar6 = (uint)bVar1;
          iVar7 = 0xffd0;
          if (((bVar1 & 0xf8) != 0x30) && ((bVar1 & 0xfe) != 0x38)) {
            uVar6 = uVar6 | 0x20;
            if (5 < uVar6 - 0x61) goto LAB_005ac1a8;
            iVar7 = 0xffa9;
          }
          if (param_4 != 0) {
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4);
            return param_2 + 3;
          }
          FUN_005ac1ac(param_1,iVar7 + uVar6 + (iVar5 + uVar4 + iVar3) * 0x10);
          return param_2 + 3;
        }
      }
LAB_005ac1a8:
                    /* WARNING: Subroutine does not return */
      FUN_005abb94();
    }
    if (bVar1 == 0x72) {
      if (param_4 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,0xd);
        goto LAB_005ac194;
      }
      uVar2 = 0xd;
    }
    else {
      if (bVar1 != 0x74) goto LAB_005ac168;
      if (param_4 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEaSEc(param_4,9);
        goto LAB_005ac194;
      }
      uVar2 = 9;
    }
  }
LAB_005ac190:
  FUN_005ac1ac(param_1,uVar2);
LAB_005ac194:
  return param_2 + 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005abeac"></a> `005abeac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005abeb0"></a> `005abeb0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005abeb4"></a> `005abeb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005abeb8"></a> `005abeb8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-005abebc"></a> `005abebc` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-005abec0"></a> `005abec0` | `c0 16 00 54` | b.eq 0x005ac198 | `CONDITIONAL_JUMP`
<a id="insn-005abec4"></a> `005abec4` | `61 02 40 39` | ldrb w1,[x19] | `FALL_THROUGH`
<a id="insn-005abec8"></a> `005abec8` | `3f c4 01 71` | cmp w1,#0x71 | `FALL_THROUGH`
<a id="insn-005abecc"></a> `005abecc` | `6d 01 00 54` | b.le 0x005abef8 | `CONDITIONAL_JUMP`
<a id="insn-005abed0"></a> `005abed0` | `3f d0 01 71` | cmp w1,#0x74 | `FALL_THROUGH`
<a id="insn-005abed4"></a> `005abed4` | `cd 03 00 54` | b.le 0x005abf4c | `CONDITIONAL_JUMP`
<a id="insn-005abed8"></a> `005abed8` | `3f d4 01 71` | cmp w1,#0x75 | `FALL_THROUGH`
<a id="insn-005abedc"></a> `005abedc` | `a0 07 00 54` | b.eq 0x005abfd0 | `CONDITIONAL_JUMP`
<a id="insn-005abee0"></a> `005abee0` | `3f d8 01 71` | cmp w1,#0x76 | `FALL_THROUGH`
<a id="insn-005abee4"></a> `005abee4` | `20 06 00 54` | b.eq 0x005abfa8 | `CONDITIONAL_JUMP`
<a id="insn-005abee8"></a> `005abee8` | `3f e0 01 71` | cmp w1,#0x78 | `FALL_THROUGH`
<a id="insn-005abeec"></a> `005abeec` | `e1 13 00 54` | b.ne 0x005ac168 | `CONDITIONAL_JUMP`
<a id="insn-005abef0"></a> `005abef0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-005abef4"></a> `005abef4` | `5b 00 00 14` | b 0x005ac060 | `UNCONDITIONAL_JUMP`
<a id="insn-005abef8"></a> `005abef8` | `3f 94 01 71` | cmp w1,#0x65 | `FALL_THROUGH`
<a id="insn-005abefc"></a> `005abefc` | `ac 03 00 54` | b.gt 0x005abf70 | `CONDITIONAL_JUMP`
<a id="insn-005abf00"></a> `005abf00` | `3f c0 00 71` | cmp w1,#0x30 | `FALL_THROUGH`
<a id="insn-005abf04"></a> `005abf04` | `c0 05 00 54` | b.eq 0x005abfbc | `CONDITIONAL_JUMP`
<a id="insn-005abf08"></a> `005abf08` | `3f 8c 01 71` | cmp w1,#0x63 | `FALL_THROUGH`
<a id="insn-005abf0c"></a> `005abf0c` | `a1 12 00 54` | b.ne 0x005ac160 | `CONDITIONAL_JUMP`
<a id="insn-005abf10"></a> `005abf10` | `68 06 00 91` | add x8,x19,#0x1 | `FALL_THROUGH`
<a id="insn-005abf14"></a> `005abf14` | `1f 01 02 eb` | cmp x8,x2 | `FALL_THROUGH`
<a id="insn-005abf18"></a> `005abf18` | `80 14 00 54` | b.eq 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005abf1c"></a> `005abf1c` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-005abf20"></a> `005abf20` | `09 79 1a 12` | and w9,w8,#0xffffffdf | `FALL_THROUGH`
<a id="insn-005abf24"></a> `005abf24` | `29 05 01 51` | sub w9,w9,#0x41 | `FALL_THROUGH`
<a id="insn-005abf28"></a> `005abf28` | `29 1d 00 12` | and w9,w9,#0xff | `FALL_THROUGH`
<a id="insn-005abf2c"></a> `005abf2c` | `3f 65 00 71` | cmp w9,#0x19 | `FALL_THROUGH`
<a id="insn-005abf30"></a> `005abf30` | `c8 13 00 54` | b.hi 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005abf34"></a> `005abf34` | `01 11 00 12` | and w1,w8,#0x1f | `FALL_THROUGH`
<a id="insn-005abf38"></a> `005abf38` | `e3 10 00 b4` | cbz x3,0x005ac154 | `CONDITIONAL_JUMP`
<a id="insn-005abf3c"></a> `005abf3c` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005abf40"></a> `005abf40` | `80 c6 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005abf44"></a> `005abf44` | `73 0a 00 91` | add x19,x19,#0x2 | `FALL_THROUGH`
<a id="insn-005abf48"></a> `005abf48` | `94 00 00 14` | b 0x005ac198 | `UNCONDITIONAL_JUMP`
<a id="insn-005abf4c"></a> `005abf4c` | `3f c8 01 71` | cmp w1,#0x72 | `FALL_THROUGH`
<a id="insn-005abf50"></a> `005abf50` | `20 02 00 54` | b.eq 0x005abf94 | `CONDITIONAL_JUMP`
<a id="insn-005abf54"></a> `005abf54` | `3f d0 01 71` | cmp w1,#0x74 | `FALL_THROUGH`
<a id="insn-005abf58"></a> `005abf58` | `81 10 00 54` | b.ne 0x005ac168 | `CONDITIONAL_JUMP`
<a id="insn-005abf5c"></a> `005abf5c` | `c3 0e 00 b4` | cbz x3,0x005ac134 | `CONDITIONAL_JUMP`
<a id="insn-005abf60"></a> `005abf60` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005abf64"></a> `005abf64` | `21 01 80 52` | mov w1,#0x9 | `FALL_THROUGH`
<a id="insn-005abf68"></a> `005abf68` | `76 c6 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005abf6c"></a> `005abf6c` | `8a 00 00 14` | b 0x005ac194 | `UNCONDITIONAL_JUMP`
<a id="insn-005abf70"></a> `005abf70` | `3f 98 01 71` | cmp w1,#0x66 | `FALL_THROUGH`
<a id="insn-005abf74"></a> `005abf74` | `80 0c 00 54` | b.eq 0x005ac104 | `CONDITIONAL_JUMP`
<a id="insn-005abf78"></a> `005abf78` | `3f b8 01 71` | cmp w1,#0x6e | `FALL_THROUGH`
<a id="insn-005abf7c"></a> `005abf7c` | `61 0f 00 54` | b.ne 0x005ac168 | `CONDITIONAL_JUMP`
<a id="insn-005abf80"></a> `005abf80` | `63 0e 00 b4` | cbz x3,0x005ac14c | `CONDITIONAL_JUMP`
<a id="insn-005abf84"></a> `005abf84` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005abf88"></a> `005abf88` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-005abf8c"></a> `005abf8c` | `6d c6 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005abf90"></a> `005abf90` | `81 00 00 14` | b 0x005ac194 | `UNCONDITIONAL_JUMP`
<a id="insn-005abf94"></a> `005abf94` | `83 0c 00 b4` | cbz x3,0x005ac124 | `CONDITIONAL_JUMP`
<a id="insn-005abf98"></a> `005abf98` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005abf9c"></a> `005abf9c` | `a1 01 80 52` | mov w1,#0xd | `FALL_THROUGH`
<a id="insn-005abfa0"></a> `005abfa0` | `68 c6 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005abfa4"></a> `005abfa4` | `7c 00 00 14` | b 0x005ac194 | `UNCONDITIONAL_JUMP`
<a id="insn-005abfa8"></a> `005abfa8` | `23 0c 00 b4` | cbz x3,0x005ac12c | `CONDITIONAL_JUMP`
<a id="insn-005abfac"></a> `005abfac` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005abfb0"></a> `005abfb0` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-005abfb4"></a> `005abfb4` | `63 c6 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005abfb8"></a> `005abfb8` | `77 00 00 14` | b 0x005ac194 | `UNCONDITIONAL_JUMP`
<a id="insn-005abfbc"></a> `005abfbc` | `03 0c 00 b4` | cbz x3,0x005ac13c | `CONDITIONAL_JUMP`
<a id="insn-005abfc0"></a> `005abfc0` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005abfc4"></a> `005abfc4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-005abfc8"></a> `005abfc8` | `5e c6 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005abfcc"></a> `005abfcc` | `72 00 00 14` | b 0x005ac194 | `UNCONDITIONAL_JUMP`
<a id="insn-005abfd0"></a> `005abfd0` | `68 06 00 91` | add x8,x19,#0x1 | `FALL_THROUGH`
<a id="insn-005abfd4"></a> `005abfd4` | `1f 01 02 eb` | cmp x8,x2 | `FALL_THROUGH`
<a id="insn-005abfd8"></a> `005abfd8` | `80 0e 00 54` | b.eq 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005abfdc"></a> `005abfdc` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-005abfe0"></a> `005abfe0` | `09 11 1d 12` | and w9,w8,#0xf8 | `FALL_THROUGH`
<a id="insn-005abfe4"></a> `005abfe4` | `3f c1 00 71` | cmp w9,#0x30 | `FALL_THROUGH`
<a id="insn-005abfe8"></a> `005abfe8` | `09 fa 9f 52` | mov w9,#0xffd0 | `FALL_THROUGH`
<a id="insn-005abfec"></a> `005abfec` | `20 01 00 54` | b.eq 0x005ac010 | `CONDITIONAL_JUMP`
<a id="insn-005abff0"></a> `005abff0` | `0a 19 1f 12` | and w10,w8,#0xfe | `FALL_THROUGH`
<a id="insn-005abff4"></a> `005abff4` | `5f e1 00 71` | cmp w10,#0x38 | `FALL_THROUGH`
<a id="insn-005abff8"></a> `005abff8` | `c0 00 00 54` | b.eq 0x005ac010 | `CONDITIONAL_JUMP`
<a id="insn-005abffc"></a> `005abffc` | `08 01 1b 32` | orr w8,w8,#0x20 | `FALL_THROUGH`
<a id="insn-005ac000"></a> `005ac000` | `09 85 01 51` | sub w9,w8,#0x61 | `FALL_THROUGH`
<a id="insn-005ac004"></a> `005ac004` | `3f 19 00 71` | cmp w9,#0x6 | `FALL_THROUGH`
<a id="insn-005ac008"></a> `005ac008` | `02 0d 00 54` | b.cs 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac00c"></a> `005ac00c` | `29 f5 9f 52` | mov w9,#0xffa9 | `FALL_THROUGH`
<a id="insn-005ac010"></a> `005ac010` | `73 0a 00 91` | add x19,x19,#0x2 | `FALL_THROUGH`
<a id="insn-005ac014"></a> `005ac014` | `7f 02 02 eb` | cmp x19,x2 | `FALL_THROUGH`
<a id="insn-005ac018"></a> `005ac018` | `80 0c 00 54` | b.eq 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac01c"></a> `005ac01c` | `6a 02 40 39` | ldrb w10,[x19] | `FALL_THROUGH`
<a id="insn-005ac020"></a> `005ac020` | `4b 11 1d 12` | and w11,w10,#0xf8 | `FALL_THROUGH`
<a id="insn-005ac024"></a> `005ac024` | `7f c1 00 71` | cmp w11,#0x30 | `FALL_THROUGH`
<a id="insn-005ac028"></a> `005ac028` | `0b fa 9f 52` | mov w11,#0xffd0 | `FALL_THROUGH`
<a id="insn-005ac02c"></a> `005ac02c` | `20 01 00 54` | b.eq 0x005ac050 | `CONDITIONAL_JUMP`
<a id="insn-005ac030"></a> `005ac030` | `4c 19 1f 12` | and w12,w10,#0xfe | `FALL_THROUGH`
<a id="insn-005ac034"></a> `005ac034` | `9f e1 00 71` | cmp w12,#0x38 | `FALL_THROUGH`
<a id="insn-005ac038"></a> `005ac038` | `c0 00 00 54` | b.eq 0x005ac050 | `CONDITIONAL_JUMP`
<a id="insn-005ac03c"></a> `005ac03c` | `4a 01 1b 32` | orr w10,w10,#0x20 | `FALL_THROUGH`
<a id="insn-005ac040"></a> `005ac040` | `4b 85 01 51` | sub w11,w10,#0x61 | `FALL_THROUGH`
<a id="insn-005ac044"></a> `005ac044` | `7f 19 00 71` | cmp w11,#0x6 | `FALL_THROUGH`
<a id="insn-005ac048"></a> `005ac048` | `02 0b 00 54` | b.cs 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac04c"></a> `005ac04c` | `2b f5 9f 52` | mov w11,#0xffa9 | `FALL_THROUGH`
<a id="insn-005ac050"></a> `005ac050` | `28 01 08 0b` | add w8,w9,w8 | `FALL_THROUGH`
<a id="insn-005ac054"></a> `005ac054` | `69 01 0a 0b` | add w9,w11,w10 | `FALL_THROUGH`
<a id="insn-005ac058"></a> `005ac058` | `08 5d 18 53` | lsl w8,w8,#0x8 | `FALL_THROUGH`
<a id="insn-005ac05c"></a> `005ac05c` | `08 11 09 0b` | add w8,w8,w9, LSL #0x4 | `FALL_THROUGH`
<a id="insn-005ac060"></a> `005ac060` | `69 06 00 91` | add x9,x19,#0x1 | `FALL_THROUGH`
<a id="insn-005ac064"></a> `005ac064` | `3f 01 02 eb` | cmp x9,x2 | `FALL_THROUGH`
<a id="insn-005ac068"></a> `005ac068` | `00 0a 00 54` | b.eq 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac06c"></a> `005ac06c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-005ac070"></a> `005ac070` | `2a 11 1d 12` | and w10,w9,#0xf8 | `FALL_THROUGH`
<a id="insn-005ac074"></a> `005ac074` | `5f c1 00 71` | cmp w10,#0x30 | `FALL_THROUGH`
<a id="insn-005ac078"></a> `005ac078` | `0a fa 9f 52` | mov w10,#0xffd0 | `FALL_THROUGH`
<a id="insn-005ac07c"></a> `005ac07c` | `20 01 00 54` | b.eq 0x005ac0a0 | `CONDITIONAL_JUMP`
<a id="insn-005ac080"></a> `005ac080` | `2b 19 1f 12` | and w11,w9,#0xfe | `FALL_THROUGH`
<a id="insn-005ac084"></a> `005ac084` | `7f e1 00 71` | cmp w11,#0x38 | `FALL_THROUGH`
<a id="insn-005ac088"></a> `005ac088` | `c0 00 00 54` | b.eq 0x005ac0a0 | `CONDITIONAL_JUMP`
<a id="insn-005ac08c"></a> `005ac08c` | `29 01 1b 32` | orr w9,w9,#0x20 | `FALL_THROUGH`
<a id="insn-005ac090"></a> `005ac090` | `2a 85 01 51` | sub w10,w9,#0x61 | `FALL_THROUGH`
<a id="insn-005ac094"></a> `005ac094` | `5f 19 00 71` | cmp w10,#0x6 | `FALL_THROUGH`
<a id="insn-005ac098"></a> `005ac098` | `82 08 00 54` | b.cs 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac09c"></a> `005ac09c` | `2a f5 9f 52` | mov w10,#0xffa9 | `FALL_THROUGH`
<a id="insn-005ac0a0"></a> `005ac0a0` | `6b 0a 00 91` | add x11,x19,#0x2 | `FALL_THROUGH`
<a id="insn-005ac0a4"></a> `005ac0a4` | `7f 01 02 eb` | cmp x11,x2 | `FALL_THROUGH`
<a id="insn-005ac0a8"></a> `005ac0a8` | `00 08 00 54` | b.eq 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac0ac"></a> `005ac0ac` | `6b 01 40 39` | ldrb w11,[x11] | `FALL_THROUGH`
<a id="insn-005ac0b0"></a> `005ac0b0` | `6c 11 1d 12` | and w12,w11,#0xf8 | `FALL_THROUGH`
<a id="insn-005ac0b4"></a> `005ac0b4` | `9f c1 00 71` | cmp w12,#0x30 | `FALL_THROUGH`
<a id="insn-005ac0b8"></a> `005ac0b8` | `0c fa 9f 52` | mov w12,#0xffd0 | `FALL_THROUGH`
<a id="insn-005ac0bc"></a> `005ac0bc` | `20 01 00 54` | b.eq 0x005ac0e0 | `CONDITIONAL_JUMP`
<a id="insn-005ac0c0"></a> `005ac0c0` | `6d 19 1f 12` | and w13,w11,#0xfe | `FALL_THROUGH`
<a id="insn-005ac0c4"></a> `005ac0c4` | `bf e1 00 71` | cmp w13,#0x38 | `FALL_THROUGH`
<a id="insn-005ac0c8"></a> `005ac0c8` | `c0 00 00 54` | b.eq 0x005ac0e0 | `CONDITIONAL_JUMP`
<a id="insn-005ac0cc"></a> `005ac0cc` | `6b 01 1b 32` | orr w11,w11,#0x20 | `FALL_THROUGH`
<a id="insn-005ac0d0"></a> `005ac0d0` | `6c 85 01 51` | sub w12,w11,#0x61 | `FALL_THROUGH`
<a id="insn-005ac0d4"></a> `005ac0d4` | `9f 19 00 71` | cmp w12,#0x6 | `FALL_THROUGH`
<a id="insn-005ac0d8"></a> `005ac0d8` | `82 06 00 54` | b.cs 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac0dc"></a> `005ac0dc` | `2c f5 9f 52` | mov w12,#0xffa9 | `FALL_THROUGH`
<a id="insn-005ac0e0"></a> `005ac0e0` | `28 01 08 0b` | add w8,w9,w8 | `FALL_THROUGH`
<a id="insn-005ac0e4"></a> `005ac0e4` | `89 01 0b 0b` | add w9,w12,w11 | `FALL_THROUGH`
<a id="insn-005ac0e8"></a> `005ac0e8` | `48 01 08 0b` | add w8,w10,w8 | `FALL_THROUGH`
<a id="insn-005ac0ec"></a> `005ac0ec` | `21 11 08 0b` | add w1,w9,w8, LSL #0x4 | `FALL_THROUGH`
<a id="insn-005ac0f0"></a> `005ac0f0` | `43 01 00 b4` | cbz x3,0x005ac118 | `CONDITIONAL_JUMP`
<a id="insn-005ac0f4"></a> `005ac0f4` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005ac0f8"></a> `005ac0f8` | `12 c6 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005ac0fc"></a> `005ac0fc` | `73 0e 00 91` | add x19,x19,#0x3 | `FALL_THROUGH`
<a id="insn-005ac100"></a> `005ac100` | `26 00 00 14` | b 0x005ac198 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac104"></a> `005ac104` | `03 02 00 b4` | cbz x3,0x005ac144 | `CONDITIONAL_JUMP`
<a id="insn-005ac108"></a> `005ac108` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005ac10c"></a> `005ac10c` | `81 01 80 52` | mov w1,#0xc | `FALL_THROUGH`
<a id="insn-005ac110"></a> `005ac110` | `0c c6 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005ac114"></a> `005ac114` | `20 00 00 14` | b 0x005ac194 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac118"></a> `005ac118` | `25 00 00 94` | bl 0x005ac1ac | `UNCONDITIONAL_CALL`
<a id="insn-005ac11c"></a> `005ac11c` | `73 0e 00 91` | add x19,x19,#0x3 | `FALL_THROUGH`
<a id="insn-005ac120"></a> `005ac120` | `1e 00 00 14` | b 0x005ac198 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac124"></a> `005ac124` | `a1 01 80 52` | mov w1,#0xd | `FALL_THROUGH`
<a id="insn-005ac128"></a> `005ac128` | `1a 00 00 14` | b 0x005ac190 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac12c"></a> `005ac12c` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-005ac130"></a> `005ac130` | `18 00 00 14` | b 0x005ac190 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac134"></a> `005ac134` | `21 01 80 52` | mov w1,#0x9 | `FALL_THROUGH`
<a id="insn-005ac138"></a> `005ac138` | `16 00 00 14` | b 0x005ac190 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac13c"></a> `005ac13c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-005ac140"></a> `005ac140` | `14 00 00 14` | b 0x005ac190 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac144"></a> `005ac144` | `81 01 80 52` | mov w1,#0xc | `FALL_THROUGH`
<a id="insn-005ac148"></a> `005ac148` | `12 00 00 14` | b 0x005ac190 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac14c"></a> `005ac14c` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-005ac150"></a> `005ac150` | `10 00 00 14` | b 0x005ac190 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac154"></a> `005ac154` | `16 00 00 94` | bl 0x005ac1ac | `UNCONDITIONAL_CALL`
<a id="insn-005ac158"></a> `005ac158` | `73 0a 00 91` | add x19,x19,#0x2 | `FALL_THROUGH`
<a id="insn-005ac15c"></a> `005ac15c` | `0f 00 00 14` | b 0x005ac198 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac160"></a> `005ac160` | `3f 7c 01 71` | cmp w1,#0x5f | `FALL_THROUGH`
<a id="insn-005ac164"></a> `005ac164` | `20 02 00 54` | b.eq 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac168"></a> `005ac168` | `c1 00 38 37` | tbnz w1,#0x7,0x005ac180 | `CONDITIONAL_JUMP`
<a id="insn-005ac16c"></a> `005ac16c` | `08 04 40 f9` | ldr x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-005ac170"></a> `005ac170` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-005ac174"></a> `005ac174` | `08 79 61 f8` | ldr x8,[x8, x1, LSL #0x3] | `FALL_THROUGH`
<a id="insn-005ac178"></a> `005ac178` | `1f 05 7b f2` | tst x8,#0x60 | `FALL_THROUGH`
<a id="insn-005ac17c"></a> `005ac17c` | `61 01 00 54` | b.ne 0x005ac1a8 | `CONDITIONAL_JUMP`
<a id="insn-005ac180"></a> `005ac180` | `83 00 00 b4` | cbz x3,0x005ac190 | `CONDITIONAL_JUMP`
<a id="insn-005ac184"></a> `005ac184` | `e0 03 03 aa` | mov x0,x3 | `FALL_THROUGH`
<a id="insn-005ac188"></a> `005ac188` | `ee c5 18 94` | bl 0x00bdd940 | `UNCONDITIONAL_CALL`
<a id="insn-005ac18c"></a> `005ac18c` | `02 00 00 14` | b 0x005ac194 | `UNCONDITIONAL_JUMP`
<a id="insn-005ac190"></a> `005ac190` | `07 00 00 94` | bl 0x005ac1ac | `UNCONDITIONAL_CALL`
<a id="insn-005ac194"></a> `005ac194` | `73 06 00 91` | add x19,x19,#0x1 | `FALL_THROUGH`
<a id="insn-005ac198"></a> `005ac198` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005ac19c"></a> `005ac19c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005ac1a0"></a> `005ac1a0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-005ac1a4"></a> `005ac1a4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-005ac1a8"></a> `005ac1a8` | `7b fe ff 97` | bl 0x005abb94 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005abeac`](#insn-005abeac) 範囲 `[['005abeac', '005abec3']]`
  - `CONDITIONAL_JUMP` [`005abec0`](#insn-005abec0) → [`005ac198`](#insn-005ac198)
  - `FALL_THROUGH` [`005abec0`](#insn-005abec0) → [`005abec4`](#insn-005abec4)
- ブロック [`005abec4`](#insn-005abec4) 範囲 `[['005abec4', '005abecf']]`
  - `CONDITIONAL_JUMP` [`005abecc`](#insn-005abecc) → [`005abef8`](#insn-005abef8)
  - `FALL_THROUGH` [`005abecc`](#insn-005abecc) → [`005abed0`](#insn-005abed0)
- ブロック [`005abed0`](#insn-005abed0) 範囲 `[['005abed0', '005abed7']]`
  - `CONDITIONAL_JUMP` [`005abed4`](#insn-005abed4) → [`005abf4c`](#insn-005abf4c)
  - `FALL_THROUGH` [`005abed4`](#insn-005abed4) → [`005abed8`](#insn-005abed8)
- ブロック [`005abed8`](#insn-005abed8) 範囲 `[['005abed8', '005abedf']]`
  - `CONDITIONAL_JUMP` [`005abedc`](#insn-005abedc) → [`005abfd0`](#insn-005abfd0)
  - `FALL_THROUGH` [`005abedc`](#insn-005abedc) → [`005abee0`](#insn-005abee0)
- ブロック [`005abee0`](#insn-005abee0) 範囲 `[['005abee0', '005abee7']]`
  - `CONDITIONAL_JUMP` [`005abee4`](#insn-005abee4) → [`005abfa8`](#insn-005abfa8)
  - `FALL_THROUGH` [`005abee4`](#insn-005abee4) → [`005abee8`](#insn-005abee8)
- ブロック [`005abee8`](#insn-005abee8) 範囲 `[['005abee8', '005abeef']]`
  - `CONDITIONAL_JUMP` [`005abeec`](#insn-005abeec) → [`005ac168`](#insn-005ac168)
  - `FALL_THROUGH` [`005abeec`](#insn-005abeec) → [`005abef0`](#insn-005abef0)
- ブロック [`005abef0`](#insn-005abef0) 範囲 `[['005abef0', '005abef7']]`
  - `UNCONDITIONAL_JUMP` [`005abef4`](#insn-005abef4) → [`005ac060`](#insn-005ac060)
- ブロック [`005abef8`](#insn-005abef8) 範囲 `[['005abef8', '005abeff']]`
  - `CONDITIONAL_JUMP` [`005abefc`](#insn-005abefc) → [`005abf70`](#insn-005abf70)
  - `FALL_THROUGH` [`005abefc`](#insn-005abefc) → [`005abf00`](#insn-005abf00)
- ブロック [`005abf00`](#insn-005abf00) 範囲 `[['005abf00', '005abf07']]`
  - `CONDITIONAL_JUMP` [`005abf04`](#insn-005abf04) → [`005abfbc`](#insn-005abfbc)
  - `FALL_THROUGH` [`005abf04`](#insn-005abf04) → [`005abf08`](#insn-005abf08)
- ブロック [`005abf08`](#insn-005abf08) 範囲 `[['005abf08', '005abf0f']]`
  - `CONDITIONAL_JUMP` [`005abf0c`](#insn-005abf0c) → [`005ac160`](#insn-005ac160)
  - `FALL_THROUGH` [`005abf0c`](#insn-005abf0c) → [`005abf10`](#insn-005abf10)
- ブロック [`005abf10`](#insn-005abf10) 範囲 `[['005abf10', '005abf1b']]`
  - `CONDITIONAL_JUMP` [`005abf18`](#insn-005abf18) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005abf18`](#insn-005abf18) → [`005abf1c`](#insn-005abf1c)
- ブロック [`005abf1c`](#insn-005abf1c) 範囲 `[['005abf1c', '005abf33']]`
  - `CONDITIONAL_JUMP` [`005abf30`](#insn-005abf30) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005abf30`](#insn-005abf30) → [`005abf34`](#insn-005abf34)
- ブロック [`005abf34`](#insn-005abf34) 範囲 `[['005abf34', '005abf3b']]`
  - `CONDITIONAL_JUMP` [`005abf38`](#insn-005abf38) → [`005ac154`](#insn-005ac154)
  - `FALL_THROUGH` [`005abf38`](#insn-005abf38) → [`005abf3c`](#insn-005abf3c)
- ブロック [`005abf3c`](#insn-005abf3c) 範囲 `[['005abf3c', '005abf4b']]`
  - `UNCONDITIONAL_JUMP` [`005abf48`](#insn-005abf48) → [`005ac198`](#insn-005ac198)
- ブロック [`005abf4c`](#insn-005abf4c) 範囲 `[['005abf4c', '005abf53']]`
  - `CONDITIONAL_JUMP` [`005abf50`](#insn-005abf50) → [`005abf94`](#insn-005abf94)
  - `FALL_THROUGH` [`005abf50`](#insn-005abf50) → [`005abf54`](#insn-005abf54)
- ブロック [`005abf54`](#insn-005abf54) 範囲 `[['005abf54', '005abf5b']]`
  - `CONDITIONAL_JUMP` [`005abf58`](#insn-005abf58) → [`005ac168`](#insn-005ac168)
  - `FALL_THROUGH` [`005abf58`](#insn-005abf58) → [`005abf5c`](#insn-005abf5c)
- ブロック [`005abf5c`](#insn-005abf5c) 範囲 `[['005abf5c', '005abf5f']]`
  - `CONDITIONAL_JUMP` [`005abf5c`](#insn-005abf5c) → [`005ac134`](#insn-005ac134)
  - `FALL_THROUGH` [`005abf5c`](#insn-005abf5c) → [`005abf60`](#insn-005abf60)
- ブロック [`005abf60`](#insn-005abf60) 範囲 `[['005abf60', '005abf6f']]`
  - `UNCONDITIONAL_JUMP` [`005abf6c`](#insn-005abf6c) → [`005ac194`](#insn-005ac194)
- ブロック [`005abf70`](#insn-005abf70) 範囲 `[['005abf70', '005abf77']]`
  - `CONDITIONAL_JUMP` [`005abf74`](#insn-005abf74) → [`005ac104`](#insn-005ac104)
  - `FALL_THROUGH` [`005abf74`](#insn-005abf74) → [`005abf78`](#insn-005abf78)
- ブロック [`005abf78`](#insn-005abf78) 範囲 `[['005abf78', '005abf7f']]`
  - `CONDITIONAL_JUMP` [`005abf7c`](#insn-005abf7c) → [`005ac168`](#insn-005ac168)
  - `FALL_THROUGH` [`005abf7c`](#insn-005abf7c) → [`005abf80`](#insn-005abf80)
- ブロック [`005abf80`](#insn-005abf80) 範囲 `[['005abf80', '005abf83']]`
  - `CONDITIONAL_JUMP` [`005abf80`](#insn-005abf80) → [`005ac14c`](#insn-005ac14c)
  - `FALL_THROUGH` [`005abf80`](#insn-005abf80) → [`005abf84`](#insn-005abf84)
- ブロック [`005abf84`](#insn-005abf84) 範囲 `[['005abf84', '005abf93']]`
  - `UNCONDITIONAL_JUMP` [`005abf90`](#insn-005abf90) → [`005ac194`](#insn-005ac194)
- ブロック [`005abf94`](#insn-005abf94) 範囲 `[['005abf94', '005abf97']]`
  - `CONDITIONAL_JUMP` [`005abf94`](#insn-005abf94) → [`005ac124`](#insn-005ac124)
  - `FALL_THROUGH` [`005abf94`](#insn-005abf94) → [`005abf98`](#insn-005abf98)
- ブロック [`005abf98`](#insn-005abf98) 範囲 `[['005abf98', '005abfa7']]`
  - `UNCONDITIONAL_JUMP` [`005abfa4`](#insn-005abfa4) → [`005ac194`](#insn-005ac194)
- ブロック [`005abfa8`](#insn-005abfa8) 範囲 `[['005abfa8', '005abfab']]`
  - `CONDITIONAL_JUMP` [`005abfa8`](#insn-005abfa8) → [`005ac12c`](#insn-005ac12c)
  - `FALL_THROUGH` [`005abfa8`](#insn-005abfa8) → [`005abfac`](#insn-005abfac)
- ブロック [`005abfac`](#insn-005abfac) 範囲 `[['005abfac', '005abfbb']]`
  - `UNCONDITIONAL_JUMP` [`005abfb8`](#insn-005abfb8) → [`005ac194`](#insn-005ac194)
- ブロック [`005abfbc`](#insn-005abfbc) 範囲 `[['005abfbc', '005abfbf']]`
  - `CONDITIONAL_JUMP` [`005abfbc`](#insn-005abfbc) → [`005ac13c`](#insn-005ac13c)
  - `FALL_THROUGH` [`005abfbc`](#insn-005abfbc) → [`005abfc0`](#insn-005abfc0)
- ブロック [`005abfc0`](#insn-005abfc0) 範囲 `[['005abfc0', '005abfcf']]`
  - `UNCONDITIONAL_JUMP` [`005abfcc`](#insn-005abfcc) → [`005ac194`](#insn-005ac194)
- ブロック [`005abfd0`](#insn-005abfd0) 範囲 `[['005abfd0', '005abfdb']]`
  - `CONDITIONAL_JUMP` [`005abfd8`](#insn-005abfd8) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005abfd8`](#insn-005abfd8) → [`005abfdc`](#insn-005abfdc)
- ブロック [`005abfdc`](#insn-005abfdc) 範囲 `[['005abfdc', '005abfef']]`
  - `CONDITIONAL_JUMP` [`005abfec`](#insn-005abfec) → [`005ac010`](#insn-005ac010)
  - `FALL_THROUGH` [`005abfec`](#insn-005abfec) → [`005abff0`](#insn-005abff0)
- ブロック [`005abff0`](#insn-005abff0) 範囲 `[['005abff0', '005abffb']]`
  - `CONDITIONAL_JUMP` [`005abff8`](#insn-005abff8) → [`005ac010`](#insn-005ac010)
  - `FALL_THROUGH` [`005abff8`](#insn-005abff8) → [`005abffc`](#insn-005abffc)
- ブロック [`005abffc`](#insn-005abffc) 範囲 `[['005abffc', '005ac00b']]`
  - `CONDITIONAL_JUMP` [`005ac008`](#insn-005ac008) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac008`](#insn-005ac008) → [`005ac00c`](#insn-005ac00c)
- ブロック [`005ac00c`](#insn-005ac00c) 範囲 `[['005ac00c', '005ac00f']]`
  - `FALL_THROUGH` [`005ac00c`](#insn-005ac00c) → [`005ac010`](#insn-005ac010)
- ブロック [`005ac010`](#insn-005ac010) 範囲 `[['005ac010', '005ac01b']]`
  - `CONDITIONAL_JUMP` [`005ac018`](#insn-005ac018) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac018`](#insn-005ac018) → [`005ac01c`](#insn-005ac01c)
- ブロック [`005ac01c`](#insn-005ac01c) 範囲 `[['005ac01c', '005ac02f']]`
  - `CONDITIONAL_JUMP` [`005ac02c`](#insn-005ac02c) → [`005ac050`](#insn-005ac050)
  - `FALL_THROUGH` [`005ac02c`](#insn-005ac02c) → [`005ac030`](#insn-005ac030)
- ブロック [`005ac030`](#insn-005ac030) 範囲 `[['005ac030', '005ac03b']]`
  - `CONDITIONAL_JUMP` [`005ac038`](#insn-005ac038) → [`005ac050`](#insn-005ac050)
  - `FALL_THROUGH` [`005ac038`](#insn-005ac038) → [`005ac03c`](#insn-005ac03c)
- ブロック [`005ac03c`](#insn-005ac03c) 範囲 `[['005ac03c', '005ac04b']]`
  - `CONDITIONAL_JUMP` [`005ac048`](#insn-005ac048) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac048`](#insn-005ac048) → [`005ac04c`](#insn-005ac04c)
- ブロック [`005ac04c`](#insn-005ac04c) 範囲 `[['005ac04c', '005ac04f']]`
  - `FALL_THROUGH` [`005ac04c`](#insn-005ac04c) → [`005ac050`](#insn-005ac050)
- ブロック [`005ac050`](#insn-005ac050) 範囲 `[['005ac050', '005ac05f']]`
  - `FALL_THROUGH` [`005ac05c`](#insn-005ac05c) → [`005ac060`](#insn-005ac060)
- ブロック [`005ac060`](#insn-005ac060) 範囲 `[['005ac060', '005ac06b']]`
  - `CONDITIONAL_JUMP` [`005ac068`](#insn-005ac068) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac068`](#insn-005ac068) → [`005ac06c`](#insn-005ac06c)
- ブロック [`005ac06c`](#insn-005ac06c) 範囲 `[['005ac06c', '005ac07f']]`
  - `CONDITIONAL_JUMP` [`005ac07c`](#insn-005ac07c) → [`005ac0a0`](#insn-005ac0a0)
  - `FALL_THROUGH` [`005ac07c`](#insn-005ac07c) → [`005ac080`](#insn-005ac080)
- ブロック [`005ac080`](#insn-005ac080) 範囲 `[['005ac080', '005ac08b']]`
  - `CONDITIONAL_JUMP` [`005ac088`](#insn-005ac088) → [`005ac0a0`](#insn-005ac0a0)
  - `FALL_THROUGH` [`005ac088`](#insn-005ac088) → [`005ac08c`](#insn-005ac08c)
- ブロック [`005ac08c`](#insn-005ac08c) 範囲 `[['005ac08c', '005ac09b']]`
  - `CONDITIONAL_JUMP` [`005ac098`](#insn-005ac098) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac098`](#insn-005ac098) → [`005ac09c`](#insn-005ac09c)
- ブロック [`005ac09c`](#insn-005ac09c) 範囲 `[['005ac09c', '005ac09f']]`
  - `FALL_THROUGH` [`005ac09c`](#insn-005ac09c) → [`005ac0a0`](#insn-005ac0a0)
- ブロック [`005ac0a0`](#insn-005ac0a0) 範囲 `[['005ac0a0', '005ac0ab']]`
  - `CONDITIONAL_JUMP` [`005ac0a8`](#insn-005ac0a8) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac0a8`](#insn-005ac0a8) → [`005ac0ac`](#insn-005ac0ac)
- ブロック [`005ac0ac`](#insn-005ac0ac) 範囲 `[['005ac0ac', '005ac0bf']]`
  - `CONDITIONAL_JUMP` [`005ac0bc`](#insn-005ac0bc) → [`005ac0e0`](#insn-005ac0e0)
  - `FALL_THROUGH` [`005ac0bc`](#insn-005ac0bc) → [`005ac0c0`](#insn-005ac0c0)
- ブロック [`005ac0c0`](#insn-005ac0c0) 範囲 `[['005ac0c0', '005ac0cb']]`
  - `CONDITIONAL_JUMP` [`005ac0c8`](#insn-005ac0c8) → [`005ac0e0`](#insn-005ac0e0)
  - `FALL_THROUGH` [`005ac0c8`](#insn-005ac0c8) → [`005ac0cc`](#insn-005ac0cc)
- ブロック [`005ac0cc`](#insn-005ac0cc) 範囲 `[['005ac0cc', '005ac0db']]`
  - `CONDITIONAL_JUMP` [`005ac0d8`](#insn-005ac0d8) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac0d8`](#insn-005ac0d8) → [`005ac0dc`](#insn-005ac0dc)
- ブロック [`005ac0dc`](#insn-005ac0dc) 範囲 `[['005ac0dc', '005ac0df']]`
  - `FALL_THROUGH` [`005ac0dc`](#insn-005ac0dc) → [`005ac0e0`](#insn-005ac0e0)
- ブロック [`005ac0e0`](#insn-005ac0e0) 範囲 `[['005ac0e0', '005ac0f3']]`
  - `CONDITIONAL_JUMP` [`005ac0f0`](#insn-005ac0f0) → [`005ac118`](#insn-005ac118)
  - `FALL_THROUGH` [`005ac0f0`](#insn-005ac0f0) → [`005ac0f4`](#insn-005ac0f4)
- ブロック [`005ac0f4`](#insn-005ac0f4) 範囲 `[['005ac0f4', '005ac103']]`
  - `UNCONDITIONAL_JUMP` [`005ac100`](#insn-005ac100) → [`005ac198`](#insn-005ac198)
- ブロック [`005ac104`](#insn-005ac104) 範囲 `[['005ac104', '005ac107']]`
  - `CONDITIONAL_JUMP` [`005ac104`](#insn-005ac104) → [`005ac144`](#insn-005ac144)
  - `FALL_THROUGH` [`005ac104`](#insn-005ac104) → [`005ac108`](#insn-005ac108)
- ブロック [`005ac108`](#insn-005ac108) 範囲 `[['005ac108', '005ac117']]`
  - `UNCONDITIONAL_JUMP` [`005ac114`](#insn-005ac114) → [`005ac194`](#insn-005ac194)
- ブロック [`005ac118`](#insn-005ac118) 範囲 `[['005ac118', '005ac123']]`
  - `UNCONDITIONAL_JUMP` [`005ac120`](#insn-005ac120) → [`005ac198`](#insn-005ac198)
- ブロック [`005ac124`](#insn-005ac124) 範囲 `[['005ac124', '005ac12b']]`
  - `UNCONDITIONAL_JUMP` [`005ac128`](#insn-005ac128) → [`005ac190`](#insn-005ac190)
- ブロック [`005ac12c`](#insn-005ac12c) 範囲 `[['005ac12c', '005ac133']]`
  - `UNCONDITIONAL_JUMP` [`005ac130`](#insn-005ac130) → [`005ac190`](#insn-005ac190)
- ブロック [`005ac134`](#insn-005ac134) 範囲 `[['005ac134', '005ac13b']]`
  - `UNCONDITIONAL_JUMP` [`005ac138`](#insn-005ac138) → [`005ac190`](#insn-005ac190)
- ブロック [`005ac13c`](#insn-005ac13c) 範囲 `[['005ac13c', '005ac143']]`
  - `UNCONDITIONAL_JUMP` [`005ac140`](#insn-005ac140) → [`005ac190`](#insn-005ac190)
- ブロック [`005ac144`](#insn-005ac144) 範囲 `[['005ac144', '005ac14b']]`
  - `UNCONDITIONAL_JUMP` [`005ac148`](#insn-005ac148) → [`005ac190`](#insn-005ac190)
- ブロック [`005ac14c`](#insn-005ac14c) 範囲 `[['005ac14c', '005ac153']]`
  - `UNCONDITIONAL_JUMP` [`005ac150`](#insn-005ac150) → [`005ac190`](#insn-005ac190)
- ブロック [`005ac154`](#insn-005ac154) 範囲 `[['005ac154', '005ac15f']]`
  - `UNCONDITIONAL_JUMP` [`005ac15c`](#insn-005ac15c) → [`005ac198`](#insn-005ac198)
- ブロック [`005ac160`](#insn-005ac160) 範囲 `[['005ac160', '005ac167']]`
  - `CONDITIONAL_JUMP` [`005ac164`](#insn-005ac164) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac164`](#insn-005ac164) → [`005ac168`](#insn-005ac168)
- ブロック [`005ac168`](#insn-005ac168) 範囲 `[['005ac168', '005ac16b']]`
  - `CONDITIONAL_JUMP` [`005ac168`](#insn-005ac168) → [`005ac180`](#insn-005ac180)
  - `FALL_THROUGH` [`005ac168`](#insn-005ac168) → [`005ac16c`](#insn-005ac16c)
- ブロック [`005ac16c`](#insn-005ac16c) 範囲 `[['005ac16c', '005ac17f']]`
  - `CONDITIONAL_JUMP` [`005ac17c`](#insn-005ac17c) → [`005ac1a8`](#insn-005ac1a8)
  - `FALL_THROUGH` [`005ac17c`](#insn-005ac17c) → [`005ac180`](#insn-005ac180)
- ブロック [`005ac180`](#insn-005ac180) 範囲 `[['005ac180', '005ac183']]`
  - `CONDITIONAL_JUMP` [`005ac180`](#insn-005ac180) → [`005ac190`](#insn-005ac190)
  - `FALL_THROUGH` [`005ac180`](#insn-005ac180) → [`005ac184`](#insn-005ac184)
- ブロック [`005ac184`](#insn-005ac184) 範囲 `[['005ac184', '005ac18f']]`
  - `UNCONDITIONAL_JUMP` [`005ac18c`](#insn-005ac18c) → [`005ac194`](#insn-005ac194)
- ブロック [`005ac190`](#insn-005ac190) 範囲 `[['005ac190', '005ac193']]`
  - `FALL_THROUGH` [`005ac190`](#insn-005ac190) → [`005ac194`](#insn-005ac194)
- ブロック [`005ac194`](#insn-005ac194) 範囲 `[['005ac194', '005ac197']]`
  - `FALL_THROUGH` [`005ac194`](#insn-005ac194) → [`005ac198`](#insn-005ac198)
- ブロック [`005ac198`](#insn-005ac198) 範囲 `[['005ac198', '005ac1a7']]`
- ブロック [`005ac1a8`](#insn-005ac1a8) 範囲 `[['005ac1a8', '005ac1ab']]`

## 命令位置別の参照

- [`005abeac`](#insn-005abeac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abeb0`](#insn-005abeb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abec0`](#insn-005abec0) → [`005ac198`](#insn-005ac198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abecc`](#insn-005abecc) → [`005abef8`](#insn-005abef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abed4`](#insn-005abed4) → [`005abf4c`](#insn-005abf4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abedc`](#insn-005abedc) → [`005abfd0`](#insn-005abfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abee4`](#insn-005abee4) → [`005abfa8`](#insn-005abfa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abeec`](#insn-005abeec) → [`005ac168`](#insn-005ac168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abef4`](#insn-005abef4) → [`005ac060`](#insn-005ac060) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abefc`](#insn-005abefc) → [`005abf70`](#insn-005abf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf04`](#insn-005abf04) → [`005abfbc`](#insn-005abfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf0c`](#insn-005abf0c) → [`005ac160`](#insn-005ac160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf18`](#insn-005abf18) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf30`](#insn-005abf30) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf38`](#insn-005abf38) → [`005ac154`](#insn-005ac154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf40`](#insn-005abf40) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005abf48`](#insn-005abf48) → [`005ac198`](#insn-005ac198) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf50`](#insn-005abf50) → [`005abf94`](#insn-005abf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf58`](#insn-005abf58) → [`005ac168`](#insn-005ac168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf5c`](#insn-005abf5c) → [`005ac134`](#insn-005ac134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf68`](#insn-005abf68) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005abf6c`](#insn-005abf6c) → [`005ac194`](#insn-005ac194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf74`](#insn-005abf74) → [`005ac104`](#insn-005ac104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf7c`](#insn-005abf7c) → [`005ac168`](#insn-005ac168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf80`](#insn-005abf80) → [`005ac14c`](#insn-005ac14c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf8c`](#insn-005abf8c) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005abf90`](#insn-005abf90) → [`005ac194`](#insn-005ac194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abf94`](#insn-005abf94) → [`005ac124`](#insn-005ac124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abfa0`](#insn-005abfa0) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005abfa4`](#insn-005abfa4) → [`005ac194`](#insn-005ac194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abfa8`](#insn-005abfa8) → [`005ac12c`](#insn-005ac12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abfb4`](#insn-005abfb4) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005abfb8`](#insn-005abfb8) → [`005ac194`](#insn-005ac194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abfbc`](#insn-005abfbc) → [`005ac13c`](#insn-005ac13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abfc8`](#insn-005abfc8) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005abfcc`](#insn-005abfcc) → [`005ac194`](#insn-005ac194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abfd8`](#insn-005abfd8) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abfec`](#insn-005abfec) → [`005ac010`](#insn-005ac010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005abff8`](#insn-005abff8) → [`005ac010`](#insn-005ac010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac008`](#insn-005ac008) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac018`](#insn-005ac018) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac02c`](#insn-005ac02c) → [`005ac050`](#insn-005ac050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac038`](#insn-005ac038) → [`005ac050`](#insn-005ac050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac048`](#insn-005ac048) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac068`](#insn-005ac068) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac07c`](#insn-005ac07c) → [`005ac0a0`](#insn-005ac0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac088`](#insn-005ac088) → [`005ac0a0`](#insn-005ac0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac098`](#insn-005ac098) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac0a8`](#insn-005ac0a8) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac0bc`](#insn-005ac0bc) → [`005ac0e0`](#insn-005ac0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac0c8`](#insn-005ac0c8) → [`005ac0e0`](#insn-005ac0e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac0d8`](#insn-005ac0d8) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac0f0`](#insn-005ac0f0) → [`005ac118`](#insn-005ac118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac0f8`](#insn-005ac0f8) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005ac100`](#insn-005ac100) → [`005ac198`](#insn-005ac198) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac104`](#insn-005ac104) → [`005ac144`](#insn-005ac144) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac110`](#insn-005ac110) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005ac114`](#insn-005ac114) → [`005ac194`](#insn-005ac194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac118`](#insn-005ac118) → [`005ac1ac`](../005ac/005ac1ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005ac1ac` · 推定シンボル `None` · 推定型 `None`
- [`005ac120`](#insn-005ac120) → [`005ac198`](#insn-005ac198) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac128`](#insn-005ac128) → [`005ac190`](#insn-005ac190) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac130`](#insn-005ac130) → [`005ac190`](#insn-005ac190) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac138`](#insn-005ac138) → [`005ac190`](#insn-005ac190) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac140`](#insn-005ac140) → [`005ac190`](#insn-005ac190) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac148`](#insn-005ac148) → [`005ac190`](#insn-005ac190) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac150`](#insn-005ac150) → [`005ac190`](#insn-005ac190) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac154`](#insn-005ac154) → [`005ac1ac`](../005ac/005ac1ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005ac1ac` · 推定シンボル `None` · 推定型 `None`
- [`005ac15c`](#insn-005ac15c) → [`005ac198`](#insn-005ac198) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac164`](#insn-005ac164) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac168`](#insn-005ac168) → [`005ac180`](#insn-005ac180) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac17c`](#insn-005ac17c) → [`005ac1a8`](#insn-005ac1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac180`](#insn-005ac180) → [`005ac190`](#insn-005ac190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac188`](#insn-005ac188) → [`00bdd940`](../00bdd/00bdd940.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd940` · 推定シンボル `None` · 推定型 `None`
- [`005ac18c`](#insn-005ac18c) → [`005ac194`](#insn-005ac194) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac190`](#insn-005ac190) → [`005ac1ac`](../005ac/005ac1ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005ac1ac` · 推定シンボル `None` · 推定型 `None`
- [`005ac19c`](#insn-005ac19c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac1a0`](#insn-005ac1a0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005ac1a8`](#insn-005ac1a8) → [`005abb94`](005abb94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005abb94` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005abeac`](#insn-005abeac)

~~~json
{
  "source": "005abeac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abeb0`](#insn-005abeb0)

~~~json
{
  "source": "005abeb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abec0`](#insn-005abec0)

~~~json
{
  "source": "005abec0",
  "target": "005ac198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abecc`](#insn-005abecc)

~~~json
{
  "source": "005abecc",
  "target": "005abef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abed4`](#insn-005abed4)

~~~json
{
  "source": "005abed4",
  "target": "005abf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abedc`](#insn-005abedc)

~~~json
{
  "source": "005abedc",
  "target": "005abfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abee4`](#insn-005abee4)

~~~json
{
  "source": "005abee4",
  "target": "005abfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abeec`](#insn-005abeec)

~~~json
{
  "source": "005abeec",
  "target": "005ac168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abef4`](#insn-005abef4)

~~~json
{
  "source": "005abef4",
  "target": "005ac060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abefc`](#insn-005abefc)

~~~json
{
  "source": "005abefc",
  "target": "005abf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf04`](#insn-005abf04)

~~~json
{
  "source": "005abf04",
  "target": "005abfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf0c`](#insn-005abf0c)

~~~json
{
  "source": "005abf0c",
  "target": "005ac160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf18`](#insn-005abf18)

~~~json
{
  "source": "005abf18",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf30`](#insn-005abf30)

~~~json
{
  "source": "005abf30",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf38`](#insn-005abf38)

~~~json
{
  "source": "005abf38",
  "target": "005ac154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf40`](#insn-005abf40)

~~~json
{
  "source": "005abf40",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005abf48`](#insn-005abf48)

~~~json
{
  "source": "005abf48",
  "target": "005ac198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf50`](#insn-005abf50)

~~~json
{
  "source": "005abf50",
  "target": "005abf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf58`](#insn-005abf58)

~~~json
{
  "source": "005abf58",
  "target": "005ac168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf5c`](#insn-005abf5c)

~~~json
{
  "source": "005abf5c",
  "target": "005ac134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf68`](#insn-005abf68)

~~~json
{
  "source": "005abf68",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005abf6c`](#insn-005abf6c)

~~~json
{
  "source": "005abf6c",
  "target": "005ac194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf74`](#insn-005abf74)

~~~json
{
  "source": "005abf74",
  "target": "005ac104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf7c`](#insn-005abf7c)

~~~json
{
  "source": "005abf7c",
  "target": "005ac168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf80`](#insn-005abf80)

~~~json
{
  "source": "005abf80",
  "target": "005ac14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf8c`](#insn-005abf8c)

~~~json
{
  "source": "005abf8c",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005abf90`](#insn-005abf90)

~~~json
{
  "source": "005abf90",
  "target": "005ac194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abf94`](#insn-005abf94)

~~~json
{
  "source": "005abf94",
  "target": "005ac124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abfa0`](#insn-005abfa0)

~~~json
{
  "source": "005abfa0",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005abfa4`](#insn-005abfa4)

~~~json
{
  "source": "005abfa4",
  "target": "005ac194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abfa8`](#insn-005abfa8)

~~~json
{
  "source": "005abfa8",
  "target": "005ac12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abfb4`](#insn-005abfb4)

~~~json
{
  "source": "005abfb4",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005abfb8`](#insn-005abfb8)

~~~json
{
  "source": "005abfb8",
  "target": "005ac194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abfbc`](#insn-005abfbc)

~~~json
{
  "source": "005abfbc",
  "target": "005ac13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abfc8`](#insn-005abfc8)

~~~json
{
  "source": "005abfc8",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005abfcc`](#insn-005abfcc)

~~~json
{
  "source": "005abfcc",
  "target": "005ac194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abfd8`](#insn-005abfd8)

~~~json
{
  "source": "005abfd8",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abfec`](#insn-005abfec)

~~~json
{
  "source": "005abfec",
  "target": "005ac010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005abff8`](#insn-005abff8)

~~~json
{
  "source": "005abff8",
  "target": "005ac010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac008`](#insn-005ac008)

~~~json
{
  "source": "005ac008",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac018`](#insn-005ac018)

~~~json
{
  "source": "005ac018",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac02c`](#insn-005ac02c)

~~~json
{
  "source": "005ac02c",
  "target": "005ac050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac038`](#insn-005ac038)

~~~json
{
  "source": "005ac038",
  "target": "005ac050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac048`](#insn-005ac048)

~~~json
{
  "source": "005ac048",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac068`](#insn-005ac068)

~~~json
{
  "source": "005ac068",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac07c`](#insn-005ac07c)

~~~json
{
  "source": "005ac07c",
  "target": "005ac0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac088`](#insn-005ac088)

~~~json
{
  "source": "005ac088",
  "target": "005ac0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac098`](#insn-005ac098)

~~~json
{
  "source": "005ac098",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac0a8`](#insn-005ac0a8)

~~~json
{
  "source": "005ac0a8",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac0bc`](#insn-005ac0bc)

~~~json
{
  "source": "005ac0bc",
  "target": "005ac0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac0c8`](#insn-005ac0c8)

~~~json
{
  "source": "005ac0c8",
  "target": "005ac0e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac0d8`](#insn-005ac0d8)

~~~json
{
  "source": "005ac0d8",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac0f0`](#insn-005ac0f0)

~~~json
{
  "source": "005ac0f0",
  "target": "005ac118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac0f8`](#insn-005ac0f8)

~~~json
{
  "source": "005ac0f8",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005ac100`](#insn-005ac100)

~~~json
{
  "source": "005ac100",
  "target": "005ac198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac104`](#insn-005ac104)

~~~json
{
  "source": "005ac104",
  "target": "005ac144",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac110`](#insn-005ac110)

~~~json
{
  "source": "005ac110",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005ac114`](#insn-005ac114)

~~~json
{
  "source": "005ac114",
  "target": "005ac194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac118`](#insn-005ac118)

~~~json
{
  "source": "005ac118",
  "target": "005ac1ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005ac120`](#insn-005ac120)

~~~json
{
  "source": "005ac120",
  "target": "005ac198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac128`](#insn-005ac128)

~~~json
{
  "source": "005ac128",
  "target": "005ac190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac130`](#insn-005ac130)

~~~json
{
  "source": "005ac130",
  "target": "005ac190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac138`](#insn-005ac138)

~~~json
{
  "source": "005ac138",
  "target": "005ac190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac140`](#insn-005ac140)

~~~json
{
  "source": "005ac140",
  "target": "005ac190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac148`](#insn-005ac148)

~~~json
{
  "source": "005ac148",
  "target": "005ac190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac150`](#insn-005ac150)

~~~json
{
  "source": "005ac150",
  "target": "005ac190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac154`](#insn-005ac154)

~~~json
{
  "source": "005ac154",
  "target": "005ac1ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005ac15c`](#insn-005ac15c)

~~~json
{
  "source": "005ac15c",
  "target": "005ac198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac164`](#insn-005ac164)

~~~json
{
  "source": "005ac164",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac168`](#insn-005ac168)

~~~json
{
  "source": "005ac168",
  "target": "005ac180",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac17c`](#insn-005ac17c)

~~~json
{
  "source": "005ac17c",
  "target": "005ac1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac180`](#insn-005ac180)

~~~json
{
  "source": "005ac180",
  "target": "005ac190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac188`](#insn-005ac188)

~~~json
{
  "source": "005ac188",
  "target": "00bdd940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005ac18c`](#insn-005ac18c)

~~~json
{
  "source": "005ac18c",
  "target": "005ac194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac190`](#insn-005ac190)

~~~json
{
  "source": "005ac190",
  "target": "005ac1ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005ac19c`](#insn-005ac19c)

~~~json
{
  "source": "005ac19c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac1a0`](#insn-005ac1a0)

~~~json
{
  "source": "005ac1a0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005ac1a8`](#insn-005ac1a8)

~~~json
{
  "source": "005ac1a8",
  "target": "005abb94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
