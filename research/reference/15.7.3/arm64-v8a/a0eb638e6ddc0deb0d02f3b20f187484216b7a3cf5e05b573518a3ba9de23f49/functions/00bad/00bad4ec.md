# 00bad4ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bad424`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad424.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-aed5b55a023155b268bb3f39e7aa7a29)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bad530`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad530.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-2592922c3c9958949261a7bcbf0629c5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bad4ec",
  "name": "_ZNKSt6__ndk114__codecvt_utf8IDsE9do_lengthER9mbstate_tPKcS5_m",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "56dd57b0f8b2b34322dfcd48638f5feba6ed217b8c702df1fbb60bafe6c104b7",
  "source_text_sha256": "56dd57b0f8b2b34322dfcd48638f5feba6ed217b8c702df1fbb60bafe6c104b7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bad4ec",
        "00bad657"
      ]
    ],
    "bytes_sha256": "1405ccaad9017b416c26f816b903d583315b2b6e4a603c6f479027d943a512e2",
    "instruction_count": 91,
    "instruction_bytes": 364,
    "body_bytes": 364,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1909 bytes

~~~c

int _ZNKSt6__ndk114__codecvt_utf8IDsE9do_lengthER9mbstate_tPKcS5_m
              (long param_1,undefined8 param_2,byte *param_3,byte *param_4,ulong param_5)

{
  long lVar1;
  byte bVar2;
  bool bVar3;
  int iVar4;
  ulong uVar5;
  ulong uVar6;
  uint uVar7;
  uint uVar8;
  uint uVar9;
  
  iVar4 = (int)param_3;
  if ((((2 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
      (*param_3 == 0xef)) && (param_3[1] == 0xbb)) {
    lVar1 = 3;
    if (param_3[2] != 0xbf) {
      lVar1 = 0;
    }
    param_3 = param_3 + lVar1;
  }
  if ((param_5 != 0) && (param_3 < param_4)) {
    uVar5 = *(ulong *)(param_1 + 0x10);
    uVar6 = 1;
    do {
      bVar2 = *param_3;
      if ((char)bVar2 < '\0') {
        if (bVar2 < 0xc2) break;
        uVar7 = (uint)bVar2;
        if (bVar2 < 0xe0) {
          if ((((long)param_4 - (long)param_3 < 2) || ((param_3[1] & 0xc0) != 0x80)) ||
             (uVar5 < (param_3[1] & 0x3f | (uVar7 & 0x1f) << 6))) break;
          param_3 = param_3 + 2;
        }
        else {
          if ((0xef < bVar2) || ((long)param_4 - (long)param_3 < 3)) break;
          uVar8 = (uint)param_3[1];
          if (bVar2 == 0xed) {
            uVar9 = uVar8 & 0xe0;
LAB_00bad610:
            if (uVar9 != 0x80) break;
          }
          else {
            if (uVar7 != 0xe0) {
              uVar9 = uVar8 & 0xc0;
              goto LAB_00bad610;
            }
            if ((uVar8 & 0xe0) != 0xa0) break;
          }
          if (((param_3[2] & 0xc0) != 0x80) ||
             (uVar5 < ((uVar7 & 0xf) << 0xc | (uVar8 & 0x3f) << 6 | param_3[2] & 0x3f))) break;
          param_3 = param_3 + 3;
        }
      }
      else {
        if (uVar5 < bVar2) break;
        param_3 = param_3 + 1;
      }
      if ((param_4 <= param_3) || (bVar3 = param_5 <= uVar6, uVar6 = uVar6 + 1, bVar3)) break;
    } while( true );
  }
  return (int)param_3 - iVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bad4ec"></a> `00bad4ec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bad4f0"></a> `00bad4f0` | `68 00 02 cb` | sub x8,x3,x2 | `FALL_THROUGH`
<a id="insn-00bad4f4"></a> `00bad4f4` | `1f 0d 00 f1` | cmp x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bad4f8"></a> `00bad4f8` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00bad4fc"></a> `00bad4fc` | `2b 02 00 54` | b.lt 0x00bad540 | `CONDITIONAL_JUMP`
<a id="insn-00bad500"></a> `00bad500` | `09 18 40 b9` | ldr w9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bad504"></a> `00bad504` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00bad508"></a> `00bad508` | `c9 01 10 36` | tbz w9,#0x2,0x00bad540 | `CONDITIONAL_JUMP`
<a id="insn-00bad50c"></a> `00bad50c` | `48 00 40 39` | ldrb w8,[x2] | `FALL_THROUGH`
<a id="insn-00bad510"></a> `00bad510` | `1f bd 03 71` | cmp w8,#0xef | `FALL_THROUGH`
<a id="insn-00bad514"></a> `00bad514` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00bad518"></a> `00bad518` | `41 01 00 54` | b.ne 0x00bad540 | `CONDITIONAL_JUMP`
<a id="insn-00bad51c"></a> `00bad51c` | `48 04 40 39` | ldrb w8,[x2, #0x1] | `FALL_THROUGH`
<a id="insn-00bad520"></a> `00bad520` | `1f ed 02 71` | cmp w8,#0xbb | `FALL_THROUGH`
<a id="insn-00bad524"></a> `00bad524` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00bad528"></a> `00bad528` | `c1 00 00 54` | b.ne 0x00bad540 | `CONDITIONAL_JUMP`
<a id="insn-00bad52c"></a> `00bad52c` | `48 08 40 39` | ldrb w8,[x2, #0x2] | `FALL_THROUGH`
<a id="insn-00bad530"></a> `00bad530` | `1f fd 02 71` | cmp w8,#0xbf | `FALL_THROUGH`
<a id="insn-00bad534"></a> `00bad534` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bad538"></a> `00bad538` | `08 01 9f 9a` | csel x8,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-00bad53c"></a> `00bad53c` | `48 00 08 8b` | add x8,x2,x8 | `FALL_THROUGH`
<a id="insn-00bad540"></a> `00bad540` | `84 08 00 b4` | cbz x4,0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad544"></a> `00bad544` | `1f 01 03 eb` | cmp x8,x3 | `FALL_THROUGH`
<a id="insn-00bad548"></a> `00bad548` | `42 08 00 54` | b.cs 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad54c"></a> `00bad54c` | `09 08 40 f9` | ldr x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bad550"></a> `00bad550` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00bad554"></a> `00bad554` | `0b 01 c0 39` | ldrsb w11,[x8] | `FALL_THROUGH`
<a id="insn-00bad558"></a> `00bad558` | `0b 01 f8 37` | tbnz w11,#0x1f,0x00bad578 | `CONDITIONAL_JUMP`
<a id="insn-00bad55c"></a> `00bad55c` | `6b 1d 40 92` | and x11,x11,#0xff | `FALL_THROUGH`
<a id="insn-00bad560"></a> `00bad560` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-00bad564"></a> `00bad564` | `63 07 00 54` | b.cc 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad568"></a> `00bad568` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bad56c"></a> `00bad56c` | `1f 01 03 eb` | cmp x8,x3 | `FALL_THROUGH`
<a id="insn-00bad570"></a> `00bad570` | `a3 06 00 54` | b.cc 0x00bad644 | `CONDITIONAL_JUMP`
<a id="insn-00bad574"></a> `00bad574` | `37 00 00 14` | b 0x00bad650 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad578"></a> `00bad578` | `6b 1d 00 12` | and w11,w11,#0xff | `FALL_THROUGH`
<a id="insn-00bad57c"></a> `00bad57c` | `7f 09 03 71` | cmp w11,#0xc2 | `FALL_THROUGH`
<a id="insn-00bad580"></a> `00bad580` | `83 06 00 54` | b.cc 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad584"></a> `00bad584` | `7f 7d 03 71` | cmp w11,#0xdf | `FALL_THROUGH`
<a id="insn-00bad588"></a> `00bad588` | `08 02 00 54` | b.hi 0x00bad5c8 | `CONDITIONAL_JUMP`
<a id="insn-00bad58c"></a> `00bad58c` | `6c 00 08 cb` | sub x12,x3,x8 | `FALL_THROUGH`
<a id="insn-00bad590"></a> `00bad590` | `9f 09 00 f1` | cmp x12,#0x2 | `FALL_THROUGH`
<a id="insn-00bad594"></a> `00bad594` | `eb 05 00 54` | b.lt 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad598"></a> `00bad598` | `0c 05 40 39` | ldrb w12,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bad59c"></a> `00bad59c` | `8d 05 1a 12` | and w13,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bad5a0"></a> `00bad5a0` | `bf 01 02 71` | cmp w13,#0x80 | `FALL_THROUGH`
<a id="insn-00bad5a4"></a> `00bad5a4` | `61 05 00 54` | b.ne 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad5a8"></a> `00bad5a8` | `8c 15 00 12` | and w12,w12,#0x3f | `FALL_THROUGH`
<a id="insn-00bad5ac"></a> `00bad5ac` | `6c 11 1a 33` | bfm w12,w11,#0x1a,#0x4 | `FALL_THROUGH`
<a id="insn-00bad5b0"></a> `00bad5b0` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00bad5b4"></a> `00bad5b4` | `e3 04 00 54` | b.cc 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad5b8"></a> `00bad5b8` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bad5bc"></a> `00bad5bc` | `1f 01 03 eb` | cmp x8,x3 | `FALL_THROUGH`
<a id="insn-00bad5c0"></a> `00bad5c0` | `23 04 00 54` | b.cc 0x00bad644 | `CONDITIONAL_JUMP`
<a id="insn-00bad5c4"></a> `00bad5c4` | `23 00 00 14` | b 0x00bad650 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad5c8"></a> `00bad5c8` | `7f bd 03 71` | cmp w11,#0xef | `FALL_THROUGH`
<a id="insn-00bad5cc"></a> `00bad5cc` | `28 04 00 54` | b.hi 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad5d0"></a> `00bad5d0` | `6c 00 08 cb` | sub x12,x3,x8 | `FALL_THROUGH`
<a id="insn-00bad5d4"></a> `00bad5d4` | `9f 0d 00 f1` | cmp x12,#0x3 | `FALL_THROUGH`
<a id="insn-00bad5d8"></a> `00bad5d8` | `cb 03 00 54` | b.lt 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad5dc"></a> `00bad5dc` | `0d 05 40 39` | ldrb w13,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bad5e0"></a> `00bad5e0` | `0c 09 40 39` | ldrb w12,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bad5e4"></a> `00bad5e4` | `7f b5 03 71` | cmp w11,#0xed | `FALL_THROUGH`
<a id="insn-00bad5e8"></a> `00bad5e8` | `e0 00 00 54` | b.eq 0x00bad604 | `CONDITIONAL_JUMP`
<a id="insn-00bad5ec"></a> `00bad5ec` | `7f 81 03 71` | cmp w11,#0xe0 | `FALL_THROUGH`
<a id="insn-00bad5f0"></a> `00bad5f0` | `e1 00 00 54` | b.ne 0x00bad60c | `CONDITIONAL_JUMP`
<a id="insn-00bad5f4"></a> `00bad5f4` | `ae 09 1b 12` | and w14,w13,#0xe0 | `FALL_THROUGH`
<a id="insn-00bad5f8"></a> `00bad5f8` | `df 81 02 71` | cmp w14,#0xa0 | `FALL_THROUGH`
<a id="insn-00bad5fc"></a> `00bad5fc` | `e0 00 00 54` | b.eq 0x00bad618 | `CONDITIONAL_JUMP`
<a id="insn-00bad600"></a> `00bad600` | `14 00 00 14` | b 0x00bad650 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad604"></a> `00bad604` | `ae 09 1b 12` | and w14,w13,#0xe0 | `FALL_THROUGH`
<a id="insn-00bad608"></a> `00bad608` | `02 00 00 14` | b 0x00bad610 | `UNCONDITIONAL_JUMP`
<a id="insn-00bad60c"></a> `00bad60c` | `ae 05 1a 12` | and w14,w13,#0xc0 | `FALL_THROUGH`
<a id="insn-00bad610"></a> `00bad610` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bad614"></a> `00bad614` | `e1 01 00 54` | b.ne 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad618"></a> `00bad618` | `8e 05 1a 12` | and w14,w12,#0xc0 | `FALL_THROUGH`
<a id="insn-00bad61c"></a> `00bad61c` | `df 01 02 71` | cmp w14,#0x80 | `FALL_THROUGH`
<a id="insn-00bad620"></a> `00bad620` | `81 01 00 54` | b.ne 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad624"></a> `00bad624` | `6b 0d 14 53` | ubfiz w11,w11,#0xc,#0x4 | `FALL_THROUGH`
<a id="insn-00bad628"></a> `00bad628` | `ab 15 1a 33` | bfm w11,w13,#0x1a,#0x5 | `FALL_THROUGH`
<a id="insn-00bad62c"></a> `00bad62c` | `8b 15 00 33` | bfxil w11,w12,#0x0,#0x6 | `FALL_THROUGH`
<a id="insn-00bad630"></a> `00bad630` | `3f 01 0b eb` | cmp x9,x11 | `FALL_THROUGH`
<a id="insn-00bad634"></a> `00bad634` | `e3 00 00 54` | b.cc 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad638"></a> `00bad638` | `08 0d 00 91` | add x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bad63c"></a> `00bad63c` | `1f 01 03 eb` | cmp x8,x3 | `FALL_THROUGH`
<a id="insn-00bad640"></a> `00bad640` | `82 00 00 54` | b.cs 0x00bad650 | `CONDITIONAL_JUMP`
<a id="insn-00bad644"></a> `00bad644` | `5f 01 04 eb` | cmp x10,x4 | `FALL_THROUGH`
<a id="insn-00bad648"></a> `00bad648` | `4a 05 00 91` | add x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bad64c"></a> `00bad64c` | `43 f8 ff 54` | b.cc 0x00bad554 | `CONDITIONAL_JUMP`
<a id="insn-00bad650"></a> `00bad650` | `00 01 02 4b` | sub w0,w8,w2 | `FALL_THROUGH`
<a id="insn-00bad654"></a> `00bad654` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bad4ec`](#insn-00bad4ec) 範囲 `[['00bad4ec', '00bad4ff']]`
  - `CONDITIONAL_JUMP` [`00bad4fc`](#insn-00bad4fc) → [`00bad540`](#insn-00bad540)
  - `FALL_THROUGH` [`00bad4fc`](#insn-00bad4fc) → [`00bad500`](#insn-00bad500)
- ブロック [`00bad500`](#insn-00bad500) 範囲 `[['00bad500', '00bad50b']]`
  - `CONDITIONAL_JUMP` [`00bad508`](#insn-00bad508) → [`00bad540`](#insn-00bad540)
  - `FALL_THROUGH` [`00bad508`](#insn-00bad508) → [`00bad50c`](#insn-00bad50c)
- ブロック [`00bad50c`](#insn-00bad50c) 範囲 `[['00bad50c', '00bad51b']]`
  - `CONDITIONAL_JUMP` [`00bad518`](#insn-00bad518) → [`00bad540`](#insn-00bad540)
  - `FALL_THROUGH` [`00bad518`](#insn-00bad518) → [`00bad51c`](#insn-00bad51c)
- ブロック [`00bad51c`](#insn-00bad51c) 範囲 `[['00bad51c', '00bad52b']]`
  - `CONDITIONAL_JUMP` [`00bad528`](#insn-00bad528) → [`00bad540`](#insn-00bad540)
  - `FALL_THROUGH` [`00bad528`](#insn-00bad528) → [`00bad52c`](#insn-00bad52c)
- ブロック [`00bad52c`](#insn-00bad52c) 範囲 `[['00bad52c', '00bad53f']]`
  - `FALL_THROUGH` [`00bad53c`](#insn-00bad53c) → [`00bad540`](#insn-00bad540)
- ブロック [`00bad540`](#insn-00bad540) 範囲 `[['00bad540', '00bad543']]`
  - `CONDITIONAL_JUMP` [`00bad540`](#insn-00bad540) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad540`](#insn-00bad540) → [`00bad544`](#insn-00bad544)
- ブロック [`00bad544`](#insn-00bad544) 範囲 `[['00bad544', '00bad54b']]`
  - `CONDITIONAL_JUMP` [`00bad548`](#insn-00bad548) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad548`](#insn-00bad548) → [`00bad54c`](#insn-00bad54c)
- ブロック [`00bad54c`](#insn-00bad54c) 範囲 `[['00bad54c', '00bad553']]`
  - `FALL_THROUGH` [`00bad550`](#insn-00bad550) → [`00bad554`](#insn-00bad554)
- ブロック [`00bad554`](#insn-00bad554) 範囲 `[['00bad554', '00bad55b']]`
  - `CONDITIONAL_JUMP` [`00bad558`](#insn-00bad558) → [`00bad578`](#insn-00bad578)
  - `FALL_THROUGH` [`00bad558`](#insn-00bad558) → [`00bad55c`](#insn-00bad55c)
- ブロック [`00bad55c`](#insn-00bad55c) 範囲 `[['00bad55c', '00bad567']]`
  - `CONDITIONAL_JUMP` [`00bad564`](#insn-00bad564) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad564`](#insn-00bad564) → [`00bad568`](#insn-00bad568)
- ブロック [`00bad568`](#insn-00bad568) 範囲 `[['00bad568', '00bad573']]`
  - `CONDITIONAL_JUMP` [`00bad570`](#insn-00bad570) → [`00bad644`](#insn-00bad644)
  - `FALL_THROUGH` [`00bad570`](#insn-00bad570) → [`00bad574`](#insn-00bad574)
- ブロック [`00bad574`](#insn-00bad574) 範囲 `[['00bad574', '00bad577']]`
  - `UNCONDITIONAL_JUMP` [`00bad574`](#insn-00bad574) → [`00bad650`](#insn-00bad650)
- ブロック [`00bad578`](#insn-00bad578) 範囲 `[['00bad578', '00bad583']]`
  - `CONDITIONAL_JUMP` [`00bad580`](#insn-00bad580) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad580`](#insn-00bad580) → [`00bad584`](#insn-00bad584)
- ブロック [`00bad584`](#insn-00bad584) 範囲 `[['00bad584', '00bad58b']]`
  - `CONDITIONAL_JUMP` [`00bad588`](#insn-00bad588) → [`00bad5c8`](#insn-00bad5c8)
  - `FALL_THROUGH` [`00bad588`](#insn-00bad588) → [`00bad58c`](#insn-00bad58c)
- ブロック [`00bad58c`](#insn-00bad58c) 範囲 `[['00bad58c', '00bad597']]`
  - `CONDITIONAL_JUMP` [`00bad594`](#insn-00bad594) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad594`](#insn-00bad594) → [`00bad598`](#insn-00bad598)
- ブロック [`00bad598`](#insn-00bad598) 範囲 `[['00bad598', '00bad5a7']]`
  - `CONDITIONAL_JUMP` [`00bad5a4`](#insn-00bad5a4) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad5a4`](#insn-00bad5a4) → [`00bad5a8`](#insn-00bad5a8)
- ブロック [`00bad5a8`](#insn-00bad5a8) 範囲 `[['00bad5a8', '00bad5b7']]`
  - `CONDITIONAL_JUMP` [`00bad5b4`](#insn-00bad5b4) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad5b4`](#insn-00bad5b4) → [`00bad5b8`](#insn-00bad5b8)
- ブロック [`00bad5b8`](#insn-00bad5b8) 範囲 `[['00bad5b8', '00bad5c3']]`
  - `CONDITIONAL_JUMP` [`00bad5c0`](#insn-00bad5c0) → [`00bad644`](#insn-00bad644)
  - `FALL_THROUGH` [`00bad5c0`](#insn-00bad5c0) → [`00bad5c4`](#insn-00bad5c4)
- ブロック [`00bad5c4`](#insn-00bad5c4) 範囲 `[['00bad5c4', '00bad5c7']]`
  - `UNCONDITIONAL_JUMP` [`00bad5c4`](#insn-00bad5c4) → [`00bad650`](#insn-00bad650)
- ブロック [`00bad5c8`](#insn-00bad5c8) 範囲 `[['00bad5c8', '00bad5cf']]`
  - `CONDITIONAL_JUMP` [`00bad5cc`](#insn-00bad5cc) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad5cc`](#insn-00bad5cc) → [`00bad5d0`](#insn-00bad5d0)
- ブロック [`00bad5d0`](#insn-00bad5d0) 範囲 `[['00bad5d0', '00bad5db']]`
  - `CONDITIONAL_JUMP` [`00bad5d8`](#insn-00bad5d8) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad5d8`](#insn-00bad5d8) → [`00bad5dc`](#insn-00bad5dc)
- ブロック [`00bad5dc`](#insn-00bad5dc) 範囲 `[['00bad5dc', '00bad5eb']]`
  - `CONDITIONAL_JUMP` [`00bad5e8`](#insn-00bad5e8) → [`00bad604`](#insn-00bad604)
  - `FALL_THROUGH` [`00bad5e8`](#insn-00bad5e8) → [`00bad5ec`](#insn-00bad5ec)
- ブロック [`00bad5ec`](#insn-00bad5ec) 範囲 `[['00bad5ec', '00bad5f3']]`
  - `CONDITIONAL_JUMP` [`00bad5f0`](#insn-00bad5f0) → [`00bad60c`](#insn-00bad60c)
  - `FALL_THROUGH` [`00bad5f0`](#insn-00bad5f0) → [`00bad5f4`](#insn-00bad5f4)
- ブロック [`00bad5f4`](#insn-00bad5f4) 範囲 `[['00bad5f4', '00bad5ff']]`
  - `CONDITIONAL_JUMP` [`00bad5fc`](#insn-00bad5fc) → [`00bad618`](#insn-00bad618)
  - `FALL_THROUGH` [`00bad5fc`](#insn-00bad5fc) → [`00bad600`](#insn-00bad600)
- ブロック [`00bad600`](#insn-00bad600) 範囲 `[['00bad600', '00bad603']]`
  - `UNCONDITIONAL_JUMP` [`00bad600`](#insn-00bad600) → [`00bad650`](#insn-00bad650)
- ブロック [`00bad604`](#insn-00bad604) 範囲 `[['00bad604', '00bad60b']]`
  - `UNCONDITIONAL_JUMP` [`00bad608`](#insn-00bad608) → [`00bad610`](#insn-00bad610)
- ブロック [`00bad60c`](#insn-00bad60c) 範囲 `[['00bad60c', '00bad60f']]`
  - `FALL_THROUGH` [`00bad60c`](#insn-00bad60c) → [`00bad610`](#insn-00bad610)
- ブロック [`00bad610`](#insn-00bad610) 範囲 `[['00bad610', '00bad617']]`
  - `CONDITIONAL_JUMP` [`00bad614`](#insn-00bad614) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad614`](#insn-00bad614) → [`00bad618`](#insn-00bad618)
- ブロック [`00bad618`](#insn-00bad618) 範囲 `[['00bad618', '00bad623']]`
  - `CONDITIONAL_JUMP` [`00bad620`](#insn-00bad620) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad620`](#insn-00bad620) → [`00bad624`](#insn-00bad624)
- ブロック [`00bad624`](#insn-00bad624) 範囲 `[['00bad624', '00bad637']]`
  - `CONDITIONAL_JUMP` [`00bad634`](#insn-00bad634) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad634`](#insn-00bad634) → [`00bad638`](#insn-00bad638)
- ブロック [`00bad638`](#insn-00bad638) 範囲 `[['00bad638', '00bad643']]`
  - `CONDITIONAL_JUMP` [`00bad640`](#insn-00bad640) → [`00bad650`](#insn-00bad650)
  - `FALL_THROUGH` [`00bad640`](#insn-00bad640) → [`00bad644`](#insn-00bad644)
- ブロック [`00bad644`](#insn-00bad644) 範囲 `[['00bad644', '00bad64f']]`
  - `CONDITIONAL_JUMP` [`00bad64c`](#insn-00bad64c) → [`00bad554`](#insn-00bad554)
  - `FALL_THROUGH` [`00bad64c`](#insn-00bad64c) → [`00bad650`](#insn-00bad650)
- ブロック [`00bad650`](#insn-00bad650) 範囲 `[['00bad650', '00bad657']]`

## 命令位置別の参照

- [`00bad4fc`](#insn-00bad4fc) → [`00bad540`](#insn-00bad540) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad508`](#insn-00bad508) → [`00bad540`](#insn-00bad540) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad518`](#insn-00bad518) → [`00bad540`](#insn-00bad540) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad528`](#insn-00bad528) → [`00bad540`](#insn-00bad540) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad540`](#insn-00bad540) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad548`](#insn-00bad548) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad558`](#insn-00bad558) → [`00bad578`](#insn-00bad578) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad564`](#insn-00bad564) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad570`](#insn-00bad570) → [`00bad644`](#insn-00bad644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad574`](#insn-00bad574) → [`00bad650`](#insn-00bad650) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad580`](#insn-00bad580) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad588`](#insn-00bad588) → [`00bad5c8`](#insn-00bad5c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad594`](#insn-00bad594) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5a4`](#insn-00bad5a4) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5b4`](#insn-00bad5b4) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5c0`](#insn-00bad5c0) → [`00bad644`](#insn-00bad644) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5c4`](#insn-00bad5c4) → [`00bad650`](#insn-00bad650) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5cc`](#insn-00bad5cc) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5d8`](#insn-00bad5d8) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5e8`](#insn-00bad5e8) → [`00bad604`](#insn-00bad604) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5f0`](#insn-00bad5f0) → [`00bad60c`](#insn-00bad60c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad5fc`](#insn-00bad5fc) → [`00bad618`](#insn-00bad618) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad600`](#insn-00bad600) → [`00bad650`](#insn-00bad650) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad608`](#insn-00bad608) → [`00bad610`](#insn-00bad610) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad614`](#insn-00bad614) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad620`](#insn-00bad620) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad634`](#insn-00bad634) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad640`](#insn-00bad640) → [`00bad650`](#insn-00bad650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bad64c`](#insn-00bad64c) → [`00bad554`](#insn-00bad554) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bad4fc`](#insn-00bad4fc)

~~~json
{
  "source": "00bad4fc",
  "target": "00bad540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad508`](#insn-00bad508)

~~~json
{
  "source": "00bad508",
  "target": "00bad540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad518`](#insn-00bad518)

~~~json
{
  "source": "00bad518",
  "target": "00bad540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad528`](#insn-00bad528)

~~~json
{
  "source": "00bad528",
  "target": "00bad540",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad540`](#insn-00bad540)

~~~json
{
  "source": "00bad540",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad548`](#insn-00bad548)

~~~json
{
  "source": "00bad548",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad558`](#insn-00bad558)

~~~json
{
  "source": "00bad558",
  "target": "00bad578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad564`](#insn-00bad564)

~~~json
{
  "source": "00bad564",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad570`](#insn-00bad570)

~~~json
{
  "source": "00bad570",
  "target": "00bad644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad574`](#insn-00bad574)

~~~json
{
  "source": "00bad574",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad580`](#insn-00bad580)

~~~json
{
  "source": "00bad580",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad588`](#insn-00bad588)

~~~json
{
  "source": "00bad588",
  "target": "00bad5c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad594`](#insn-00bad594)

~~~json
{
  "source": "00bad594",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5a4`](#insn-00bad5a4)

~~~json
{
  "source": "00bad5a4",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5b4`](#insn-00bad5b4)

~~~json
{
  "source": "00bad5b4",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5c0`](#insn-00bad5c0)

~~~json
{
  "source": "00bad5c0",
  "target": "00bad644",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5c4`](#insn-00bad5c4)

~~~json
{
  "source": "00bad5c4",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5cc`](#insn-00bad5cc)

~~~json
{
  "source": "00bad5cc",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5d8`](#insn-00bad5d8)

~~~json
{
  "source": "00bad5d8",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5e8`](#insn-00bad5e8)

~~~json
{
  "source": "00bad5e8",
  "target": "00bad604",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5f0`](#insn-00bad5f0)

~~~json
{
  "source": "00bad5f0",
  "target": "00bad60c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad5fc`](#insn-00bad5fc)

~~~json
{
  "source": "00bad5fc",
  "target": "00bad618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad600`](#insn-00bad600)

~~~json
{
  "source": "00bad600",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad608`](#insn-00bad608)

~~~json
{
  "source": "00bad608",
  "target": "00bad610",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad614`](#insn-00bad614)

~~~json
{
  "source": "00bad614",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad620`](#insn-00bad620)

~~~json
{
  "source": "00bad620",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad634`](#insn-00bad634)

~~~json
{
  "source": "00bad634",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad640`](#insn-00bad640)

~~~json
{
  "source": "00bad640",
  "target": "00bad650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bad64c`](#insn-00bad64c)

~~~json
{
  "source": "00bad64c",
  "target": "00bad554",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
