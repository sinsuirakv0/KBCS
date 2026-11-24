# 00bacaa4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baca60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bac/00baca60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/no_difference_in_scope-0019.md#compare-37f24df0955bf45c3e6a635f520ff4a1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c294ec`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c29/00c294ec.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0019.md#compare-a56e50515ba1643f7f3714c05f8faae1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bacaa4",
  "name": "FUN_00bacaa4",
  "size": 580,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95e372287260f5153b2fdf3b92d9c78fdcfe555da8b6f778665da1bb8fc8fda1",
  "source_text_sha256": "95e372287260f5153b2fdf3b92d9c78fdcfe555da8b6f778665da1bb8fc8fda1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bacaa4",
        "00bacce7"
      ]
    ],
    "bytes_sha256": "9ab2ed4263463a6217acd17e134052169087b60982f01ffe4109786ecf3862ef",
    "instruction_count": 145,
    "instruction_bytes": 580,
    "body_bytes": 580,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00baca3c](../00bac/00baca3c.md)
- [00bad070](../00bad/00bad070.md)
- [00bad198](../00bad/00bad198.md)
- [00bad728](../00bad/00bad728.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3405 bytes

~~~c

bool FUN_00bacaa4(long param_1,byte *param_2,long *param_3,long param_4,uint *param_5,long *param_6,
                 ulong param_7,uint param_8)

{
  uint uVar1;
  byte bVar2;
  uint *puVar3;
  long lVar4;
  byte *pbVar5;
  uint uVar6;
  uint uVar7;
  uint *puVar8;
  
  *param_3 = param_1;
  *param_6 = param_4;
  pbVar5 = (byte *)*param_3;
  if (((((param_8 >> 2 & 1) != 0) && (2 < (long)param_2 - (long)pbVar5)) && (*pbVar5 == 0xef)) &&
     ((pbVar5[1] == 0xbb && (pbVar5[2] == 0xbf)))) {
    pbVar5 = pbVar5 + 3;
    *param_3 = (long)pbVar5;
  }
  if (param_2 <= pbVar5) {
    return false;
  }
  puVar3 = (uint *)*param_6;
  do {
    puVar8 = puVar3;
    if (param_5 <= puVar8) break;
    bVar2 = *pbVar5;
    uVar6 = (uint)bVar2;
    if ((char)bVar2 < '\0') {
      if (uVar6 < 0xc2) {
        return (bool)2;
      }
      if (uVar6 < 0xe0) {
        if ((long)param_2 - (long)pbVar5 < 2) {
          return true;
        }
        if ((pbVar5[1] & 0xc0) != 0x80) {
          return (bool)2;
        }
        lVar4 = 2;
        uVar6 = pbVar5[1] & 0x3f | (uVar6 & 0x1f) << 6;
        if (param_7 < uVar6) {
          return (bool)2;
        }
      }
      else if (uVar6 < 0xf0) {
        if ((long)param_2 - (long)pbVar5 < 2) {
          return true;
        }
        uVar7 = (uint)pbVar5[1];
        if (uVar6 == 0xed) {
          uVar1 = uVar7 & 0xe0;
joined_r0x00bacc10:
          if (uVar1 != 0x80) {
            return (bool)2;
          }
        }
        else {
          if (uVar6 != 0xe0) {
            uVar1 = uVar7 & 0xc0;
            goto joined_r0x00bacc10;
          }
          if ((uVar7 & 0xe0) != 0xa0) {
            return (bool)2;
          }
        }
        if ((long)param_2 - (long)pbVar5 == 2) {
          return true;
        }
        if (((pbVar5[2] & 0xc0) != 0x80) ||
           (uVar6 = (uVar6 & 0xf) << 0xc | (uVar7 & 0x3f) << 6 | pbVar5[2] & 0x3f, param_7 < uVar6))
        {
          return (bool)2;
        }
        lVar4 = 3;
      }
      else {
        if (0xf4 < uVar6) {
          return (bool)2;
        }
        lVar4 = (long)param_2 - (long)pbVar5;
        if (lVar4 < 2) {
          return true;
        }
        uVar7 = (uint)pbVar5[1];
        if (uVar6 == 0xf4) {
          uVar1 = uVar7 & 0xf0;
joined_r0x00bacc60:
          if (uVar1 != 0x80) {
            return (bool)2;
          }
        }
        else {
          if (uVar6 != 0xf0) {
            uVar1 = uVar7 & 0xc0;
            goto joined_r0x00bacc60;
          }
          if (0x2f < uVar7 - 0x90) {
            return (bool)2;
          }
        }
        if (lVar4 == 2) {
          return true;
        }
        if ((pbVar5[2] & 0xc0) != 0x80) {
          return (bool)2;
        }
        if (lVar4 == 3) {
          return true;
        }
        if ((pbVar5[3] & 0xc0) != 0x80) {
          return (bool)2;
        }
        uVar6 = (uVar6 & 7) << 0x12 | (uVar7 & 0x3f) << 0xc | (pbVar5[2] & 0x3f) << 6 |
                pbVar5[3] & 0x3f;
        if (param_7 < uVar6) {
          return (bool)2;
        }
        lVar4 = 4;
      }
    }
    else {
      if (param_7 < bVar2) {
        return (bool)2;
      }
      lVar4 = 1;
    }
    *puVar8 = uVar6;
    *param_3 = (long)(pbVar5 + lVar4);
    lVar4 = *param_6;
    *param_6 = lVar4 + 4;
    pbVar5 = (byte *)*param_3;
    puVar3 = (uint *)(lVar4 + 4);
  } while (pbVar5 < param_2);
  return param_5 <= puVar8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bacaa4"></a> `00bacaa4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bacaa8"></a> `00bacaa8` | `40 00 00 f9` | str x0,[x2] | `FALL_THROUGH`
<a id="insn-00bacaac"></a> `00bacaac` | `a3 00 00 f9` | str x3,[x5] | `FALL_THROUGH`
<a id="insn-00bacab0"></a> `00bacab0` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00bacab4"></a> `00bacab4` | `e7 01 10 36` | tbz w7,#0x2,0x00bacaf0 | `CONDITIONAL_JUMP`
<a id="insn-00bacab8"></a> `00bacab8` | `29 00 08 cb` | sub x9,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacabc"></a> `00bacabc` | `3f 0d 00 f1` | cmp x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bacac0"></a> `00bacac0` | `8b 01 00 54` | b.lt 0x00bacaf0 | `CONDITIONAL_JUMP`
<a id="insn-00bacac4"></a> `00bacac4` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bacac8"></a> `00bacac8` | `3f bd 03 71` | cmp w9,#0xef | `FALL_THROUGH`
<a id="insn-00bacacc"></a> `00bacacc` | `21 01 00 54` | b.ne 0x00bacaf0 | `CONDITIONAL_JUMP`
<a id="insn-00bacad0"></a> `00bacad0` | `09 05 40 39` | ldrb w9,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bacad4"></a> `00bacad4` | `3f ed 02 71` | cmp w9,#0xbb | `FALL_THROUGH`
<a id="insn-00bacad8"></a> `00bacad8` | `c1 00 00 54` | b.ne 0x00bacaf0 | `CONDITIONAL_JUMP`
<a id="insn-00bacadc"></a> `00bacadc` | `09 09 40 39` | ldrb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bacae0"></a> `00bacae0` | `3f fd 02 71` | cmp w9,#0xbf | `FALL_THROUGH`
<a id="insn-00bacae4"></a> `00bacae4` | `61 00 00 54` | b.ne 0x00bacaf0 | `CONDITIONAL_JUMP`
<a id="insn-00bacae8"></a> `00bacae8` | `08 0d 00 91` | add x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bacaec"></a> `00bacaec` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00bacaf0"></a> `00bacaf0` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bacaf4"></a> `00bacaf4` | `82 0e 00 54` | b.cs 0x00baccc4 | `CONDITIONAL_JUMP`
<a id="insn-00bacaf8"></a> `00bacaf8` | `ab 00 40 f9` | ldr x11,[x5] | `FALL_THROUGH`
<a id="insn-00bacafc"></a> `00bacafc` | `0a 00 00 14` | b 0x00bacb24 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacb00"></a> `00bacb00` | `08 01 00 8b` | add x8,x8,x0 | `FALL_THROUGH`
<a id="insn-00bacb04"></a> `00bacb04` | `2a 01 00 b9` | str w10,[x9] | `FALL_THROUGH`
<a id="insn-00bacb08"></a> `00bacb08` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00bacb0c"></a> `00bacb0c` | `a8 00 40 f9` | ldr x8,[x5] | `FALL_THROUGH`
<a id="insn-00bacb10"></a> `00bacb10` | `0b 11 00 91` | add x11,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bacb14"></a> `00bacb14` | `ab 00 00 f9` | str x11,[x5] | `FALL_THROUGH`
<a id="insn-00bacb18"></a> `00bacb18` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00bacb1c"></a> `00bacb1c` | `1f 01 01 eb` | cmp x8,x1 | `FALL_THROUGH`
<a id="insn-00bacb20"></a> `00bacb20` | `62 0d 00 54` | b.cs 0x00bacccc | `CONDITIONAL_JUMP`
<a id="insn-00bacb24"></a> `00bacb24` | `e9 03 0b aa` | mov x9,x11 | `FALL_THROUGH`
<a id="insn-00bacb28"></a> `00bacb28` | `7f 01 04 eb` | cmp x11,x4 | `FALL_THROUGH`
<a id="insn-00bacb2c"></a> `00bacb2c` | `02 0d 00 54` | b.cs 0x00bacccc | `CONDITIONAL_JUMP`
<a id="insn-00bacb30"></a> `00bacb30` | `0b 01 c0 39` | ldrsb w11,[x8] | `FALL_THROUGH`
<a id="insn-00bacb34"></a> `00bacb34` | `6a 1d 00 12` | and w10,w11,#0xff | `FALL_THROUGH`
<a id="insn-00bacb38"></a> `00bacb38` | `cb 00 f8 37` | tbnz w11,#0x1f,0x00bacb50 | `CONDITIONAL_JUMP`
<a id="insn-00bacb3c"></a> `00bacb3c` | `6b 1d 40 92` | and x11,x11,#0xff | `FALL_THROUGH`
<a id="insn-00bacb40"></a> `00bacb40` | `7f 01 06 eb` | cmp x11,x6 | `FALL_THROUGH`
<a id="insn-00bacb44"></a> `00bacb44` | `a8 0c 00 54` | b.hi 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacb48"></a> `00bacb48` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bacb4c"></a> `00bacb4c` | `ed ff ff 17` | b 0x00bacb00 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacb50"></a> `00bacb50` | `5f 09 03 71` | cmp w10,#0xc2 | `FALL_THROUGH`
<a id="insn-00bacb54"></a> `00bacb54` | `23 0c 00 54` | b.cc 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacb58"></a> `00bacb58` | `5f 7d 03 71` | cmp w10,#0xdf | `FALL_THROUGH`
<a id="insn-00bacb5c"></a> `00bacb5c` | `e8 01 00 54` | b.hi 0x00bacb98 | `CONDITIONAL_JUMP`
<a id="insn-00bacb60"></a> `00bacb60` | `2b 00 08 cb` | sub x11,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacb64"></a> `00bacb64` | `7f 09 00 f1` | cmp x11,#0x2 | `FALL_THROUGH`
<a id="insn-00bacb68"></a> `00bacb68` | `cb 0b 00 54` | b.lt 0x00bacce0 | `CONDITIONAL_JUMP`
<a id="insn-00bacb6c"></a> `00bacb6c` | `0b 05 40 39` | ldrb w11,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bacb70"></a> `00bacb70` | `6c 05 1a 12` | and w12,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacb74"></a> `00bacb74` | `9f 01 02 71` | cmp w12,#0x80 | `FALL_THROUGH`
<a id="insn-00bacb78"></a> `00bacb78` | `01 0b 00 54` | b.ne 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacb7c"></a> `00bacb7c` | `6b 15 00 12` | and w11,w11,#0x3f | `FALL_THROUGH`
<a id="insn-00bacb80"></a> `00bacb80` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bacb84"></a> `00bacb84` | `4b 11 1a 33` | bfm w11,w10,#0x1a,#0x4 | `FALL_THROUGH`
<a id="insn-00bacb88"></a> `00bacb88` | `7f 01 06 eb` | cmp x11,x6 | `FALL_THROUGH`
<a id="insn-00bacb8c"></a> `00bacb8c` | `48 0a 00 54` | b.hi 0x00baccd4 | `CONDITIONAL_JUMP`
<a id="insn-00bacb90"></a> `00bacb90` | `ea 03 0b 2a` | mov w10,w11 | `FALL_THROUGH`
<a id="insn-00bacb94"></a> `00bacb94` | `db ff ff 17` | b 0x00bacb00 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacb98"></a> `00bacb98` | `5f bd 03 71` | cmp w10,#0xef | `FALL_THROUGH`
<a id="insn-00bacb9c"></a> `00bacb9c` | `a8 01 00 54` | b.hi 0x00bacbd0 | `CONDITIONAL_JUMP`
<a id="insn-00bacba0"></a> `00bacba0` | `2c 00 08 cb` | sub x12,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacba4"></a> `00bacba4` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bacba8"></a> `00bacba8` | `cb 09 00 54` | b.lt 0x00bacce0 | `CONDITIONAL_JUMP`
<a id="insn-00bacbac"></a> `00bacbac` | `0b 05 40 39` | ldrb w11,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bacbb0"></a> `00bacbb0` | `5f b5 03 71` | cmp w10,#0xed | `FALL_THROUGH`
<a id="insn-00bacbb4"></a> `00bacbb4` | `a0 02 00 54` | b.eq 0x00bacc08 | `CONDITIONAL_JUMP`
<a id="insn-00bacbb8"></a> `00bacbb8` | `5f 81 03 71` | cmp w10,#0xe0 | `FALL_THROUGH`
<a id="insn-00bacbbc"></a> `00bacbbc` | `e1 02 00 54` | b.ne 0x00bacc18 | `CONDITIONAL_JUMP`
<a id="insn-00bacbc0"></a> `00bacbc0` | `6d 09 1b 12` | and w13,w11,#0xe0 | `FALL_THROUGH`
<a id="insn-00bacbc4"></a> `00bacbc4` | `bf 81 02 71` | cmp w13,#0xa0 | `FALL_THROUGH`
<a id="insn-00bacbc8"></a> `00bacbc8` | `e0 02 00 54` | b.eq 0x00bacc24 | `CONDITIONAL_JUMP`
<a id="insn-00bacbcc"></a> `00bacbcc` | `43 00 00 14` | b 0x00baccd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacbd0"></a> `00bacbd0` | `5f d1 03 71` | cmp w10,#0xf4 | `FALL_THROUGH`
<a id="insn-00bacbd4"></a> `00bacbd4` | `28 08 00 54` | b.hi 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacbd8"></a> `00bacbd8` | `2c 00 08 cb` | sub x12,x1,x8 | `FALL_THROUGH`
<a id="insn-00bacbdc"></a> `00bacbdc` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bacbe0"></a> `00bacbe0` | `0b 08 00 54` | b.lt 0x00bacce0 | `CONDITIONAL_JUMP`
<a id="insn-00bacbe4"></a> `00bacbe4` | `0b 05 40 39` | ldrb w11,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bacbe8"></a> `00bacbe8` | `5f d1 03 71` | cmp w10,#0xf4 | `FALL_THROUGH`
<a id="insn-00bacbec"></a> `00bacbec` | `60 03 00 54` | b.eq 0x00bacc58 | `CONDITIONAL_JUMP`
<a id="insn-00bacbf0"></a> `00bacbf0` | `5f c1 03 71` | cmp w10,#0xf0 | `FALL_THROUGH`
<a id="insn-00bacbf4"></a> `00bacbf4` | `a1 03 00 54` | b.ne 0x00bacc68 | `CONDITIONAL_JUMP`
<a id="insn-00bacbf8"></a> `00bacbf8` | `6d 41 02 51` | sub w13,w11,#0x90 | `FALL_THROUGH`
<a id="insn-00bacbfc"></a> `00bacbfc` | `bf c1 00 71` | cmp w13,#0x30 | `FALL_THROUGH`
<a id="insn-00bacc00"></a> `00bacc00` | `a3 03 00 54` | b.cc 0x00bacc74 | `CONDITIONAL_JUMP`
<a id="insn-00bacc04"></a> `00bacc04` | `35 00 00 14` | b 0x00baccd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc08"></a> `00bacc08` | `6d 09 1b 12` | and w13,w11,#0xe0 | `FALL_THROUGH`
<a id="insn-00bacc0c"></a> `00bacc0c` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bacc10"></a> `00bacc10` | `a0 00 00 54` | b.eq 0x00bacc24 | `CONDITIONAL_JUMP`
<a id="insn-00bacc14"></a> `00bacc14` | `31 00 00 14` | b 0x00baccd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc18"></a> `00bacc18` | `6d 05 1a 12` | and w13,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacc1c"></a> `00bacc1c` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bacc20"></a> `00bacc20` | `c1 05 00 54` | b.ne 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacc24"></a> `00bacc24` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bacc28"></a> `00bacc28` | `c0 05 00 54` | b.eq 0x00bacce0 | `CONDITIONAL_JUMP`
<a id="insn-00bacc2c"></a> `00bacc2c` | `0c 09 40 39` | ldrb w12,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bacc30"></a> `00bacc30` | `8d 05 1a 12` | and w13,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacc34"></a> `00bacc34` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bacc38"></a> `00bacc38` | `01 05 00 54` | b.ne 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacc3c"></a> `00bacc3c` | `4a 0d 14 53` | ubfiz w10,w10,#0xc,#0x4 | `FALL_THROUGH`
<a id="insn-00bacc40"></a> `00bacc40` | `6a 15 1a 33` | bfm w10,w11,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00bacc44"></a> `00bacc44` | `8a 15 00 33` | bfxil w10,w12,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bacc48"></a> `00bacc48` | `5f 01 06 eb` | cmp x10,x6 | `FALL_THROUGH`
<a id="insn-00bacc4c"></a> `00bacc4c` | `68 04 00 54` | b.hi 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacc50"></a> `00bacc50` | `60 00 80 52` | mov w0,#0x3 | `FALL_THROUGH`
<a id="insn-00bacc54"></a> `00bacc54` | `ab ff ff 17` | b 0x00bacb00 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc58"></a> `00bacc58` | `6d 0d 1c 12` | and w13,w11,#0xf0 | `FALL_THROUGH`
<a id="insn-00bacc5c"></a> `00bacc5c` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bacc60"></a> `00bacc60` | `a0 00 00 54` | b.eq 0x00bacc74 | `CONDITIONAL_JUMP`
<a id="insn-00bacc64"></a> `00bacc64` | `1d 00 00 14` | b 0x00baccd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bacc68"></a> `00bacc68` | `6d 05 1a 12` | and w13,w11,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacc6c"></a> `00bacc6c` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bacc70"></a> `00bacc70` | `41 03 00 54` | b.ne 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacc74"></a> `00bacc74` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bacc78"></a> `00bacc78` | `40 03 00 54` | b.eq 0x00bacce0 | `CONDITIONAL_JUMP`
<a id="insn-00bacc7c"></a> `00bacc7c` | `0d 09 40 39` | ldrb w13,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bacc80"></a> `00bacc80` | `ae 05 1a 12` | and w14,w13,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacc84"></a> `00bacc84` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bacc88"></a> `00bacc88` | `81 02 00 54` | b.ne 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacc8c"></a> `00bacc8c` | `9f 0d 00 f1` | cmp x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bacc90"></a> `00bacc90` | `80 02 00 54` | b.eq 0x00bacce0 | `CONDITIONAL_JUMP`
<a id="insn-00bacc94"></a> `00bacc94` | `0c 0d 40 39` | ldrb w12,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00bacc98"></a> `00bacc98` | `8e 05 1a 12` | and w14,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bacc9c"></a> `00bacc9c` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bacca0"></a> `00bacca0` | `c1 01 00 54` | b.ne 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00bacca4"></a> `00bacca4` | `4a 09 0e 53` | ubfiz w10,w10,#0x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bacca8"></a> `00bacca8` | `6a 15 14 33` | bfm w10,w11,#0x14,#0x5 | `FALL_THROUGH`
<a id="insn-00baccac"></a> `00baccac` | `aa 15 1a 33` | bfm w10,w13,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00baccb0"></a> `00baccb0` | `8a 15 00 33` | bfxil w10,w12,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00baccb4"></a> `00baccb4` | `5f 01 06 eb` | cmp x10,x6 | `FALL_THROUGH`
<a id="insn-00baccb8"></a> `00baccb8` | `08 01 00 54` | b.hi 0x00baccd8 | `CONDITIONAL_JUMP`
<a id="insn-00baccbc"></a> `00baccbc` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00baccc0"></a> `00baccc0` | `90 ff ff 17` | b 0x00bacb00 | `UNCONDITIONAL_JUMP`
<a id="insn-00baccc4"></a> `00baccc4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00baccc8"></a> `00baccc8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bacccc"></a> `00bacccc` | `3f 01 04 eb` | cmp x9,x4 | `FALL_THROUGH`
<a id="insn-00baccd0"></a> `00baccd0` | `e0 37 9f 1a` | cset w0,cs | `FALL_THROUGH`
<a id="insn-00baccd4"></a> `00baccd4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00baccd8"></a> `00baccd8` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00baccdc"></a> `00baccdc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bacce0"></a> `00bacce0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bacce4"></a> `00bacce4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bacaa4`](#insn-00bacaa4) 範囲 `[['00bacaa4', '00bacab7']]`
  - `CONDITIONAL_JUMP` [`00bacab4`](#insn-00bacab4) → [`00bacaf0`](#insn-00bacaf0)
  - `FALL_THROUGH` [`00bacab4`](#insn-00bacab4) → [`00bacab8`](#insn-00bacab8)
- ブロック [`00bacab8`](#insn-00bacab8) 範囲 `[['00bacab8', '00bacac3']]`
  - `CONDITIONAL_JUMP` [`00bacac0`](#insn-00bacac0) → [`00bacaf0`](#insn-00bacaf0)
  - `FALL_THROUGH` [`00bacac0`](#insn-00bacac0) → [`00bacac4`](#insn-00bacac4)
- ブロック [`00bacac4`](#insn-00bacac4) 範囲 `[['00bacac4', '00bacacf']]`
  - `CONDITIONAL_JUMP` [`00bacacc`](#insn-00bacacc) → [`00bacaf0`](#insn-00bacaf0)
  - `FALL_THROUGH` [`00bacacc`](#insn-00bacacc) → [`00bacad0`](#insn-00bacad0)
- ブロック [`00bacad0`](#insn-00bacad0) 範囲 `[['00bacad0', '00bacadb']]`
  - `CONDITIONAL_JUMP` [`00bacad8`](#insn-00bacad8) → [`00bacaf0`](#insn-00bacaf0)
  - `FALL_THROUGH` [`00bacad8`](#insn-00bacad8) → [`00bacadc`](#insn-00bacadc)
- ブロック [`00bacadc`](#insn-00bacadc) 範囲 `[['00bacadc', '00bacae7']]`
  - `CONDITIONAL_JUMP` [`00bacae4`](#insn-00bacae4) → [`00bacaf0`](#insn-00bacaf0)
  - `FALL_THROUGH` [`00bacae4`](#insn-00bacae4) → [`00bacae8`](#insn-00bacae8)
- ブロック [`00bacae8`](#insn-00bacae8) 範囲 `[['00bacae8', '00bacaef']]`
  - `FALL_THROUGH` [`00bacaec`](#insn-00bacaec) → [`00bacaf0`](#insn-00bacaf0)
- ブロック [`00bacaf0`](#insn-00bacaf0) 範囲 `[['00bacaf0', '00bacaf7']]`
  - `CONDITIONAL_JUMP` [`00bacaf4`](#insn-00bacaf4) → [`00baccc4`](#insn-00baccc4)
  - `FALL_THROUGH` [`00bacaf4`](#insn-00bacaf4) → [`00bacaf8`](#insn-00bacaf8)
- ブロック [`00bacaf8`](#insn-00bacaf8) 範囲 `[['00bacaf8', '00bacaff']]`
  - `UNCONDITIONAL_JUMP` [`00bacafc`](#insn-00bacafc) → [`00bacb24`](#insn-00bacb24)
- ブロック [`00bacb00`](#insn-00bacb00) 範囲 `[['00bacb00', '00bacb23']]`
  - `CONDITIONAL_JUMP` [`00bacb20`](#insn-00bacb20) → [`00bacccc`](#insn-00bacccc)
  - `FALL_THROUGH` [`00bacb20`](#insn-00bacb20) → [`00bacb24`](#insn-00bacb24)
- ブロック [`00bacb24`](#insn-00bacb24) 範囲 `[['00bacb24', '00bacb2f']]`
  - `CONDITIONAL_JUMP` [`00bacb2c`](#insn-00bacb2c) → [`00bacccc`](#insn-00bacccc)
  - `FALL_THROUGH` [`00bacb2c`](#insn-00bacb2c) → [`00bacb30`](#insn-00bacb30)
- ブロック [`00bacb30`](#insn-00bacb30) 範囲 `[['00bacb30', '00bacb3b']]`
  - `CONDITIONAL_JUMP` [`00bacb38`](#insn-00bacb38) → [`00bacb50`](#insn-00bacb50)
  - `FALL_THROUGH` [`00bacb38`](#insn-00bacb38) → [`00bacb3c`](#insn-00bacb3c)
- ブロック [`00bacb3c`](#insn-00bacb3c) 範囲 `[['00bacb3c', '00bacb47']]`
  - `CONDITIONAL_JUMP` [`00bacb44`](#insn-00bacb44) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacb44`](#insn-00bacb44) → [`00bacb48`](#insn-00bacb48)
- ブロック [`00bacb48`](#insn-00bacb48) 範囲 `[['00bacb48', '00bacb4f']]`
  - `UNCONDITIONAL_JUMP` [`00bacb4c`](#insn-00bacb4c) → [`00bacb00`](#insn-00bacb00)
- ブロック [`00bacb50`](#insn-00bacb50) 範囲 `[['00bacb50', '00bacb57']]`
  - `CONDITIONAL_JUMP` [`00bacb54`](#insn-00bacb54) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacb54`](#insn-00bacb54) → [`00bacb58`](#insn-00bacb58)
- ブロック [`00bacb58`](#insn-00bacb58) 範囲 `[['00bacb58', '00bacb5f']]`
  - `CONDITIONAL_JUMP` [`00bacb5c`](#insn-00bacb5c) → [`00bacb98`](#insn-00bacb98)
  - `FALL_THROUGH` [`00bacb5c`](#insn-00bacb5c) → [`00bacb60`](#insn-00bacb60)
- ブロック [`00bacb60`](#insn-00bacb60) 範囲 `[['00bacb60', '00bacb6b']]`
  - `CONDITIONAL_JUMP` [`00bacb68`](#insn-00bacb68) → [`00bacce0`](#insn-00bacce0)
  - `FALL_THROUGH` [`00bacb68`](#insn-00bacb68) → [`00bacb6c`](#insn-00bacb6c)
- ブロック [`00bacb6c`](#insn-00bacb6c) 範囲 `[['00bacb6c', '00bacb7b']]`
  - `CONDITIONAL_JUMP` [`00bacb78`](#insn-00bacb78) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacb78`](#insn-00bacb78) → [`00bacb7c`](#insn-00bacb7c)
- ブロック [`00bacb7c`](#insn-00bacb7c) 範囲 `[['00bacb7c', '00bacb8f']]`
  - `CONDITIONAL_JUMP` [`00bacb8c`](#insn-00bacb8c) → [`00baccd4`](#insn-00baccd4)
  - `FALL_THROUGH` [`00bacb8c`](#insn-00bacb8c) → [`00bacb90`](#insn-00bacb90)
- ブロック [`00bacb90`](#insn-00bacb90) 範囲 `[['00bacb90', '00bacb97']]`
  - `UNCONDITIONAL_JUMP` [`00bacb94`](#insn-00bacb94) → [`00bacb00`](#insn-00bacb00)
- ブロック [`00bacb98`](#insn-00bacb98) 範囲 `[['00bacb98', '00bacb9f']]`
  - `CONDITIONAL_JUMP` [`00bacb9c`](#insn-00bacb9c) → [`00bacbd0`](#insn-00bacbd0)
  - `FALL_THROUGH` [`00bacb9c`](#insn-00bacb9c) → [`00bacba0`](#insn-00bacba0)
- ブロック [`00bacba0`](#insn-00bacba0) 範囲 `[['00bacba0', '00bacbab']]`
  - `CONDITIONAL_JUMP` [`00bacba8`](#insn-00bacba8) → [`00bacce0`](#insn-00bacce0)
  - `FALL_THROUGH` [`00bacba8`](#insn-00bacba8) → [`00bacbac`](#insn-00bacbac)
- ブロック [`00bacbac`](#insn-00bacbac) 範囲 `[['00bacbac', '00bacbb7']]`
  - `CONDITIONAL_JUMP` [`00bacbb4`](#insn-00bacbb4) → [`00bacc08`](#insn-00bacc08)
  - `FALL_THROUGH` [`00bacbb4`](#insn-00bacbb4) → [`00bacbb8`](#insn-00bacbb8)
- ブロック [`00bacbb8`](#insn-00bacbb8) 範囲 `[['00bacbb8', '00bacbbf']]`
  - `CONDITIONAL_JUMP` [`00bacbbc`](#insn-00bacbbc) → [`00bacc18`](#insn-00bacc18)
  - `FALL_THROUGH` [`00bacbbc`](#insn-00bacbbc) → [`00bacbc0`](#insn-00bacbc0)
- ブロック [`00bacbc0`](#insn-00bacbc0) 範囲 `[['00bacbc0', '00bacbcb']]`
  - `CONDITIONAL_JUMP` [`00bacbc8`](#insn-00bacbc8) → [`00bacc24`](#insn-00bacc24)
  - `FALL_THROUGH` [`00bacbc8`](#insn-00bacbc8) → [`00bacbcc`](#insn-00bacbcc)
- ブロック [`00bacbcc`](#insn-00bacbcc) 範囲 `[['00bacbcc', '00bacbcf']]`
  - `UNCONDITIONAL_JUMP` [`00bacbcc`](#insn-00bacbcc) → [`00baccd8`](#insn-00baccd8)
- ブロック [`00bacbd0`](#insn-00bacbd0) 範囲 `[['00bacbd0', '00bacbd7']]`
  - `CONDITIONAL_JUMP` [`00bacbd4`](#insn-00bacbd4) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacbd4`](#insn-00bacbd4) → [`00bacbd8`](#insn-00bacbd8)
- ブロック [`00bacbd8`](#insn-00bacbd8) 範囲 `[['00bacbd8', '00bacbe3']]`
  - `CONDITIONAL_JUMP` [`00bacbe0`](#insn-00bacbe0) → [`00bacce0`](#insn-00bacce0)
  - `FALL_THROUGH` [`00bacbe0`](#insn-00bacbe0) → [`00bacbe4`](#insn-00bacbe4)
- ブロック [`00bacbe4`](#insn-00bacbe4) 範囲 `[['00bacbe4', '00bacbef']]`
  - `CONDITIONAL_JUMP` [`00bacbec`](#insn-00bacbec) → [`00bacc58`](#insn-00bacc58)
  - `FALL_THROUGH` [`00bacbec`](#insn-00bacbec) → [`00bacbf0`](#insn-00bacbf0)
- ブロック [`00bacbf0`](#insn-00bacbf0) 範囲 `[['00bacbf0', '00bacbf7']]`
  - `CONDITIONAL_JUMP` [`00bacbf4`](#insn-00bacbf4) → [`00bacc68`](#insn-00bacc68)
  - `FALL_THROUGH` [`00bacbf4`](#insn-00bacbf4) → [`00bacbf8`](#insn-00bacbf8)
- ブロック [`00bacbf8`](#insn-00bacbf8) 範囲 `[['00bacbf8', '00bacc03']]`
  - `CONDITIONAL_JUMP` [`00bacc00`](#insn-00bacc00) → [`00bacc74`](#insn-00bacc74)
  - `FALL_THROUGH` [`00bacc00`](#insn-00bacc00) → [`00bacc04`](#insn-00bacc04)
- ブロック [`00bacc04`](#insn-00bacc04) 範囲 `[['00bacc04', '00bacc07']]`
  - `UNCONDITIONAL_JUMP` [`00bacc04`](#insn-00bacc04) → [`00baccd8`](#insn-00baccd8)
- ブロック [`00bacc08`](#insn-00bacc08) 範囲 `[['00bacc08', '00bacc13']]`
  - `CONDITIONAL_JUMP` [`00bacc10`](#insn-00bacc10) → [`00bacc24`](#insn-00bacc24)
  - `FALL_THROUGH` [`00bacc10`](#insn-00bacc10) → [`00bacc14`](#insn-00bacc14)
- ブロック [`00bacc14`](#insn-00bacc14) 範囲 `[['00bacc14', '00bacc17']]`
  - `UNCONDITIONAL_JUMP` [`00bacc14`](#insn-00bacc14) → [`00baccd8`](#insn-00baccd8)
- ブロック [`00bacc18`](#insn-00bacc18) 範囲 `[['00bacc18', '00bacc23']]`
  - `CONDITIONAL_JUMP` [`00bacc20`](#insn-00bacc20) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacc20`](#insn-00bacc20) → [`00bacc24`](#insn-00bacc24)
- ブロック [`00bacc24`](#insn-00bacc24) 範囲 `[['00bacc24', '00bacc2b']]`
  - `CONDITIONAL_JUMP` [`00bacc28`](#insn-00bacc28) → [`00bacce0`](#insn-00bacce0)
  - `FALL_THROUGH` [`00bacc28`](#insn-00bacc28) → [`00bacc2c`](#insn-00bacc2c)
- ブロック [`00bacc2c`](#insn-00bacc2c) 範囲 `[['00bacc2c', '00bacc3b']]`
  - `CONDITIONAL_JUMP` [`00bacc38`](#insn-00bacc38) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacc38`](#insn-00bacc38) → [`00bacc3c`](#insn-00bacc3c)
- ブロック [`00bacc3c`](#insn-00bacc3c) 範囲 `[['00bacc3c', '00bacc4f']]`
  - `CONDITIONAL_JUMP` [`00bacc4c`](#insn-00bacc4c) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacc4c`](#insn-00bacc4c) → [`00bacc50`](#insn-00bacc50)
- ブロック [`00bacc50`](#insn-00bacc50) 範囲 `[['00bacc50', '00bacc57']]`
  - `UNCONDITIONAL_JUMP` [`00bacc54`](#insn-00bacc54) → [`00bacb00`](#insn-00bacb00)
- ブロック [`00bacc58`](#insn-00bacc58) 範囲 `[['00bacc58', '00bacc63']]`
  - `CONDITIONAL_JUMP` [`00bacc60`](#insn-00bacc60) → [`00bacc74`](#insn-00bacc74)
  - `FALL_THROUGH` [`00bacc60`](#insn-00bacc60) → [`00bacc64`](#insn-00bacc64)
- ブロック [`00bacc64`](#insn-00bacc64) 範囲 `[['00bacc64', '00bacc67']]`
  - `UNCONDITIONAL_JUMP` [`00bacc64`](#insn-00bacc64) → [`00baccd8`](#insn-00baccd8)
- ブロック [`00bacc68`](#insn-00bacc68) 範囲 `[['00bacc68', '00bacc73']]`
  - `CONDITIONAL_JUMP` [`00bacc70`](#insn-00bacc70) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacc70`](#insn-00bacc70) → [`00bacc74`](#insn-00bacc74)
- ブロック [`00bacc74`](#insn-00bacc74) 範囲 `[['00bacc74', '00bacc7b']]`
  - `CONDITIONAL_JUMP` [`00bacc78`](#insn-00bacc78) → [`00bacce0`](#insn-00bacce0)
  - `FALL_THROUGH` [`00bacc78`](#insn-00bacc78) → [`00bacc7c`](#insn-00bacc7c)
- ブロック [`00bacc7c`](#insn-00bacc7c) 範囲 `[['00bacc7c', '00bacc8b']]`
  - `CONDITIONAL_JUMP` [`00bacc88`](#insn-00bacc88) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacc88`](#insn-00bacc88) → [`00bacc8c`](#insn-00bacc8c)
- ブロック [`00bacc8c`](#insn-00bacc8c) 範囲 `[['00bacc8c', '00bacc93']]`
  - `CONDITIONAL_JUMP` [`00bacc90`](#insn-00bacc90) → [`00bacce0`](#insn-00bacce0)
  - `FALL_THROUGH` [`00bacc90`](#insn-00bacc90) → [`00bacc94`](#insn-00bacc94)
- ブロック [`00bacc94`](#insn-00bacc94) 範囲 `[['00bacc94', '00bacca3']]`
  - `CONDITIONAL_JUMP` [`00bacca0`](#insn-00bacca0) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00bacca0`](#insn-00bacca0) → [`00bacca4`](#insn-00bacca4)
- ブロック [`00bacca4`](#insn-00bacca4) 範囲 `[['00bacca4', '00baccbb']]`
  - `CONDITIONAL_JUMP` [`00baccb8`](#insn-00baccb8) → [`00baccd8`](#insn-00baccd8)
  - `FALL_THROUGH` [`00baccb8`](#insn-00baccb8) → [`00baccbc`](#insn-00baccbc)
- ブロック [`00baccbc`](#insn-00baccbc) 範囲 `[['00baccbc', '00baccc3']]`
  - `UNCONDITIONAL_JUMP` [`00baccc0`](#insn-00baccc0) → [`00bacb00`](#insn-00bacb00)
- ブロック [`00baccc4`](#insn-00baccc4) 範囲 `[['00baccc4', '00bacccb']]`
- ブロック [`00bacccc`](#insn-00bacccc) 範囲 `[['00bacccc', '00baccd3']]`
  - `FALL_THROUGH` [`00baccd0`](#insn-00baccd0) → [`00baccd4`](#insn-00baccd4)
- ブロック [`00baccd4`](#insn-00baccd4) 範囲 `[['00baccd4', '00baccd7']]`
- ブロック [`00baccd8`](#insn-00baccd8) 範囲 `[['00baccd8', '00baccdf']]`
- ブロック [`00bacce0`](#insn-00bacce0) 範囲 `[['00bacce0', '00bacce7']]`

## 命令位置別の参照

- [`00bacab4`](#insn-00bacab4) → [`00bacaf0`](#insn-00bacaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacac0`](#insn-00bacac0) → [`00bacaf0`](#insn-00bacaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacacc`](#insn-00bacacc) → [`00bacaf0`](#insn-00bacaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacad8`](#insn-00bacad8) → [`00bacaf0`](#insn-00bacaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacae4`](#insn-00bacae4) → [`00bacaf0`](#insn-00bacaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacaf4`](#insn-00bacaf4) → [`00baccc4`](#insn-00baccc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacafc`](#insn-00bacafc) → [`00bacb24`](#insn-00bacb24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb20`](#insn-00bacb20) → [`00bacccc`](#insn-00bacccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb2c`](#insn-00bacb2c) → [`00bacccc`](#insn-00bacccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb38`](#insn-00bacb38) → [`00bacb50`](#insn-00bacb50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb44`](#insn-00bacb44) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb4c`](#insn-00bacb4c) → [`00bacb00`](#insn-00bacb00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb54`](#insn-00bacb54) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb5c`](#insn-00bacb5c) → [`00bacb98`](#insn-00bacb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb68`](#insn-00bacb68) → [`00bacce0`](#insn-00bacce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb78`](#insn-00bacb78) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb8c`](#insn-00bacb8c) → [`00baccd4`](#insn-00baccd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb94`](#insn-00bacb94) → [`00bacb00`](#insn-00bacb00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacb9c`](#insn-00bacb9c) → [`00bacbd0`](#insn-00bacbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacba8`](#insn-00bacba8) → [`00bacce0`](#insn-00bacce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbb4`](#insn-00bacbb4) → [`00bacc08`](#insn-00bacc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbbc`](#insn-00bacbbc) → [`00bacc18`](#insn-00bacc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbc8`](#insn-00bacbc8) → [`00bacc24`](#insn-00bacc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbcc`](#insn-00bacbcc) → [`00baccd8`](#insn-00baccd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbd4`](#insn-00bacbd4) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbe0`](#insn-00bacbe0) → [`00bacce0`](#insn-00bacce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbec`](#insn-00bacbec) → [`00bacc58`](#insn-00bacc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacbf4`](#insn-00bacbf4) → [`00bacc68`](#insn-00bacc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc00`](#insn-00bacc00) → [`00bacc74`](#insn-00bacc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc04`](#insn-00bacc04) → [`00baccd8`](#insn-00baccd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc10`](#insn-00bacc10) → [`00bacc24`](#insn-00bacc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc14`](#insn-00bacc14) → [`00baccd8`](#insn-00baccd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc20`](#insn-00bacc20) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc28`](#insn-00bacc28) → [`00bacce0`](#insn-00bacce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc38`](#insn-00bacc38) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc4c`](#insn-00bacc4c) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc54`](#insn-00bacc54) → [`00bacb00`](#insn-00bacb00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc60`](#insn-00bacc60) → [`00bacc74`](#insn-00bacc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc64`](#insn-00bacc64) → [`00baccd8`](#insn-00baccd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc70`](#insn-00bacc70) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc78`](#insn-00bacc78) → [`00bacce0`](#insn-00bacce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc88`](#insn-00bacc88) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacc90`](#insn-00bacc90) → [`00bacce0`](#insn-00bacce0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bacca0`](#insn-00bacca0) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccb8`](#insn-00baccb8) → [`00baccd8`](#insn-00baccd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baccc0`](#insn-00baccc0) → [`00bacb00`](#insn-00bacb00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bacab4`](#insn-00bacab4)

~~~json
{
  "source": "00bacab4",
  "target": "00bacaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacac0`](#insn-00bacac0)

~~~json
{
  "source": "00bacac0",
  "target": "00bacaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacacc`](#insn-00bacacc)

~~~json
{
  "source": "00bacacc",
  "target": "00bacaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacad8`](#insn-00bacad8)

~~~json
{
  "source": "00bacad8",
  "target": "00bacaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacae4`](#insn-00bacae4)

~~~json
{
  "source": "00bacae4",
  "target": "00bacaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacaf4`](#insn-00bacaf4)

~~~json
{
  "source": "00bacaf4",
  "target": "00baccc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacafc`](#insn-00bacafc)

~~~json
{
  "source": "00bacafc",
  "target": "00bacb24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb20`](#insn-00bacb20)

~~~json
{
  "source": "00bacb20",
  "target": "00bacccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb2c`](#insn-00bacb2c)

~~~json
{
  "source": "00bacb2c",
  "target": "00bacccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb38`](#insn-00bacb38)

~~~json
{
  "source": "00bacb38",
  "target": "00bacb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb44`](#insn-00bacb44)

~~~json
{
  "source": "00bacb44",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb4c`](#insn-00bacb4c)

~~~json
{
  "source": "00bacb4c",
  "target": "00bacb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb54`](#insn-00bacb54)

~~~json
{
  "source": "00bacb54",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb5c`](#insn-00bacb5c)

~~~json
{
  "source": "00bacb5c",
  "target": "00bacb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb68`](#insn-00bacb68)

~~~json
{
  "source": "00bacb68",
  "target": "00bacce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb78`](#insn-00bacb78)

~~~json
{
  "source": "00bacb78",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb8c`](#insn-00bacb8c)

~~~json
{
  "source": "00bacb8c",
  "target": "00baccd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb94`](#insn-00bacb94)

~~~json
{
  "source": "00bacb94",
  "target": "00bacb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacb9c`](#insn-00bacb9c)

~~~json
{
  "source": "00bacb9c",
  "target": "00bacbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacba8`](#insn-00bacba8)

~~~json
{
  "source": "00bacba8",
  "target": "00bacce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbb4`](#insn-00bacbb4)

~~~json
{
  "source": "00bacbb4",
  "target": "00bacc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbbc`](#insn-00bacbbc)

~~~json
{
  "source": "00bacbbc",
  "target": "00bacc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbc8`](#insn-00bacbc8)

~~~json
{
  "source": "00bacbc8",
  "target": "00bacc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbcc`](#insn-00bacbcc)

~~~json
{
  "source": "00bacbcc",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbd4`](#insn-00bacbd4)

~~~json
{
  "source": "00bacbd4",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbe0`](#insn-00bacbe0)

~~~json
{
  "source": "00bacbe0",
  "target": "00bacce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbec`](#insn-00bacbec)

~~~json
{
  "source": "00bacbec",
  "target": "00bacc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacbf4`](#insn-00bacbf4)

~~~json
{
  "source": "00bacbf4",
  "target": "00bacc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc00`](#insn-00bacc00)

~~~json
{
  "source": "00bacc00",
  "target": "00bacc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc04`](#insn-00bacc04)

~~~json
{
  "source": "00bacc04",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc10`](#insn-00bacc10)

~~~json
{
  "source": "00bacc10",
  "target": "00bacc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc14`](#insn-00bacc14)

~~~json
{
  "source": "00bacc14",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc20`](#insn-00bacc20)

~~~json
{
  "source": "00bacc20",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc28`](#insn-00bacc28)

~~~json
{
  "source": "00bacc28",
  "target": "00bacce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc38`](#insn-00bacc38)

~~~json
{
  "source": "00bacc38",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc4c`](#insn-00bacc4c)

~~~json
{
  "source": "00bacc4c",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc54`](#insn-00bacc54)

~~~json
{
  "source": "00bacc54",
  "target": "00bacb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc60`](#insn-00bacc60)

~~~json
{
  "source": "00bacc60",
  "target": "00bacc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc64`](#insn-00bacc64)

~~~json
{
  "source": "00bacc64",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc70`](#insn-00bacc70)

~~~json
{
  "source": "00bacc70",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc78`](#insn-00bacc78)

~~~json
{
  "source": "00bacc78",
  "target": "00bacce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc88`](#insn-00bacc88)

~~~json
{
  "source": "00bacc88",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacc90`](#insn-00bacc90)

~~~json
{
  "source": "00bacc90",
  "target": "00bacce0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bacca0`](#insn-00bacca0)

~~~json
{
  "source": "00bacca0",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccb8`](#insn-00baccb8)

~~~json
{
  "source": "00baccb8",
  "target": "00baccd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baccc0`](#insn-00baccc0)

~~~json
{
  "source": "00baccc0",
  "target": "00bacb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
