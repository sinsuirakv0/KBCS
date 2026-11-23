# 00baac4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baad14`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baad14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-debbf0b67ddc1e499c18bbb24278708e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baac4c",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_scan_isEmPKwS3_",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ec36b9e5437f80e35fc8decf13489e52bc7ffe01ade2ba60edce1f707635addc",
  "source_text_sha256": "ec36b9e5437f80e35fc8decf13489e52bc7ffe01ade2ba60edce1f707635addc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baac4c",
        "00baad7b"
      ]
    ],
    "bytes_sha256": "2fb68a468c2e23e3110988fddbea14f00f66840e089bb317502bc116d0538e57",
    "instruction_count": 76,
    "instruction_bytes": 304,
    "body_bytes": 304,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be18b0](../00be1/00be18b0.md)
- [00be1950](../00be1/00be1950.md)
- [00be1960](../00be1/00be1960.md)
- [00be1970](../00be1/00be1970.md)
- [00be1980](../00be1/00be1980.md)
- [00be1990](../00be1/00be1990.md)
- [00be19a0](../00be1/00be19a0.md)
- [00be19b0](../00be1/00be19b0.md)
- [00be19c0](../00be1/00be19c0.md)
- [00be19d0](../00be1/00be19d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1787 bytes

~~~c

wint_t * _ZNKSt6__ndk112ctype_bynameIwE10do_scan_isEmPKwS3_
                   (long param_1,uint param_2,wint_t *param_3,wint_t *param_4)

{
  wint_t __wc;
  int iVar1;
  
  if (param_3 != param_4) {
    while (((((__wc = *param_3, (param_2 & 1) == 0 ||
              (iVar1 = iswspace_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 == 0)) &&
             (((param_2 >> 1 & 1) == 0 ||
              (iVar1 = iswprint_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 == 0)))) &&
            (((param_2 >> 2 & 1) == 0 ||
             (iVar1 = iswcntrl_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 == 0)))) &&
           (((param_2 >> 3 & 1) == 0 ||
            (iVar1 = iswupper_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 == 0))))) {
      if (((param_2 >> 4 & 1) != 0) &&
         (iVar1 = iswlower_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 5 & 1) != 0) &&
         (iVar1 = iswalpha_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 6 & 1) != 0) &&
         (iVar1 = iswdigit_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 7 & 1) != 0) &&
         (iVar1 = iswpunct_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 8 & 1) != 0) &&
         (iVar1 = iswxdigit_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      if (((param_2 >> 9 & 1) != 0) &&
         (iVar1 = iswblank_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) {
        return param_3;
      }
      param_3 = param_3 + 1;
      if (param_3 == param_4) {
        return param_4;
      }
    }
  }
  return param_3;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baac4c"></a> `00baac4c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baac50"></a> `00baac50` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baac54"></a> `00baac54` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baac58"></a> `00baac58` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baac5c"></a> `00baac5c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baac60"></a> `00baac60` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baac64"></a> `00baac64` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00baac68"></a> `00baac68` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00baac6c"></a> `00baac6c` | `a0 07 00 54` | b.eq 0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baac70"></a> `00baac70` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00baac74"></a> `00baac74` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00baac78"></a> `00baac78` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00baac7c"></a> `00baac7c` | `04 00 00 14` | b 0x00baac8c | `UNCONDITIONAL_JUMP`
<a id="insn-00baac80"></a> `00baac80` | `73 12 00 91` | add x19,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00baac84"></a> `00baac84` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00baac88"></a> `00baac88` | `a0 06 00 54` | b.eq 0x00baad5c | `CONDITIONAL_JUMP`
<a id="insn-00baac8c"></a> `00baac8c` | `77 02 40 b9` | ldr w23,[x19] | `FALL_THROUGH`
<a id="insn-00baac90"></a> `00baac90` | `b5 00 00 36` | tbz w21,#0x0,0x00baaca4 | `CONDITIONAL_JUMP`
<a id="insn-00baac94"></a> `00baac94` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baac98"></a> `00baac98` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baac9c"></a> `00baac9c` | `2d db 00 94` | bl 0x00be1950 | `UNCONDITIONAL_CALL`
<a id="insn-00baaca0"></a> `00baaca0` | `00 06 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baaca4"></a> `00baaca4` | `b5 00 08 36` | tbz w21,#0x1,0x00baacb8 | `CONDITIONAL_JUMP`
<a id="insn-00baaca8"></a> `00baaca8` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baacac"></a> `00baacac` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baacb0"></a> `00baacb0` | `2c db 00 94` | bl 0x00be1960 | `UNCONDITIONAL_CALL`
<a id="insn-00baacb4"></a> `00baacb4` | `60 05 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baacb8"></a> `00baacb8` | `b5 00 10 36` | tbz w21,#0x2,0x00baaccc | `CONDITIONAL_JUMP`
<a id="insn-00baacbc"></a> `00baacbc` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baacc0"></a> `00baacc0` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baacc4"></a> `00baacc4` | `2f db 00 94` | bl 0x00be1980 | `UNCONDITIONAL_CALL`
<a id="insn-00baacc8"></a> `00baacc8` | `c0 04 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baaccc"></a> `00baaccc` | `b5 00 18 36` | tbz w21,#0x3,0x00baace0 | `CONDITIONAL_JUMP`
<a id="insn-00baacd0"></a> `00baacd0` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baacd4"></a> `00baacd4` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baacd8"></a> `00baacd8` | `2e db 00 94` | bl 0x00be1990 | `UNCONDITIONAL_CALL`
<a id="insn-00baacdc"></a> `00baacdc` | `20 04 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baace0"></a> `00baace0` | `b5 00 20 36` | tbz w21,#0x4,0x00baacf4 | `CONDITIONAL_JUMP`
<a id="insn-00baace4"></a> `00baace4` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baace8"></a> `00baace8` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baacec"></a> `00baacec` | `f1 da 00 94` | bl 0x00be18b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baacf0"></a> `00baacf0` | `80 03 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baacf4"></a> `00baacf4` | `b5 00 28 36` | tbz w21,#0x5,0x00baad08 | `CONDITIONAL_JUMP`
<a id="insn-00baacf8"></a> `00baacf8` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baacfc"></a> `00baacfc` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baad00"></a> `00baad00` | `28 db 00 94` | bl 0x00be19a0 | `UNCONDITIONAL_CALL`
<a id="insn-00baad04"></a> `00baad04` | `e0 02 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baad08"></a> `00baad08` | `b5 00 30 36` | tbz w21,#0x6,0x00baad1c | `CONDITIONAL_JUMP`
<a id="insn-00baad0c"></a> `00baad0c` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baad10"></a> `00baad10` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baad14"></a> `00baad14` | `27 db 00 94` | bl 0x00be19b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baad18"></a> `00baad18` | `40 02 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baad1c"></a> `00baad1c` | `b5 00 38 36` | tbz w21,#0x7,0x00baad30 | `CONDITIONAL_JUMP`
<a id="insn-00baad20"></a> `00baad20` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baad24"></a> `00baad24` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baad28"></a> `00baad28` | `26 db 00 94` | bl 0x00be19c0 | `UNCONDITIONAL_CALL`
<a id="insn-00baad2c"></a> `00baad2c` | `a0 01 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baad30"></a> `00baad30` | `b5 00 40 36` | tbz w21,#0x8,0x00baad44 | `CONDITIONAL_JUMP`
<a id="insn-00baad34"></a> `00baad34` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baad38"></a> `00baad38` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baad3c"></a> `00baad3c` | `25 db 00 94` | bl 0x00be19d0 | `UNCONDITIONAL_CALL`
<a id="insn-00baad40"></a> `00baad40` | `00 01 00 35` | cbnz w0,0x00baad60 | `CONDITIONAL_JUMP`
<a id="insn-00baad44"></a> `00baad44` | `f5 f9 4f 36` | tbz w21,#0x9,0x00baac80 | `CONDITIONAL_JUMP`
<a id="insn-00baad48"></a> `00baad48` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baad4c"></a> `00baad4c` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baad50"></a> `00baad50` | `08 db 00 94` | bl 0x00be1970 | `UNCONDITIONAL_CALL`
<a id="insn-00baad54"></a> `00baad54` | `60 f9 ff 34` | cbz w0,0x00baac80 | `CONDITIONAL_JUMP`
<a id="insn-00baad58"></a> `00baad58` | `02 00 00 14` | b 0x00baad60 | `UNCONDITIONAL_JUMP`
<a id="insn-00baad5c"></a> `00baad5c` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00baad60"></a> `00baad60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baad64"></a> `00baad64` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baad68"></a> `00baad68` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baad6c"></a> `00baad6c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baad70"></a> `00baad70` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baad74"></a> `00baad74` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baad78"></a> `00baad78` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baac4c`](#insn-00baac4c) 範囲 `[['00baac4c', '00baac6f']]`
  - `CONDITIONAL_JUMP` [`00baac6c`](#insn-00baac6c) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baac6c`](#insn-00baac6c) → [`00baac70`](#insn-00baac70)
- ブロック [`00baac70`](#insn-00baac70) 範囲 `[['00baac70', '00baac7f']]`
  - `UNCONDITIONAL_JUMP` [`00baac7c`](#insn-00baac7c) → [`00baac8c`](#insn-00baac8c)
- ブロック [`00baac80`](#insn-00baac80) 範囲 `[['00baac80', '00baac8b']]`
  - `CONDITIONAL_JUMP` [`00baac88`](#insn-00baac88) → [`00baad5c`](#insn-00baad5c)
  - `FALL_THROUGH` [`00baac88`](#insn-00baac88) → [`00baac8c`](#insn-00baac8c)
- ブロック [`00baac8c`](#insn-00baac8c) 範囲 `[['00baac8c', '00baac93']]`
  - `CONDITIONAL_JUMP` [`00baac90`](#insn-00baac90) → [`00baaca4`](#insn-00baaca4)
  - `FALL_THROUGH` [`00baac90`](#insn-00baac90) → [`00baac94`](#insn-00baac94)
- ブロック [`00baac94`](#insn-00baac94) 範囲 `[['00baac94', '00baaca3']]`
  - `CONDITIONAL_JUMP` [`00baaca0`](#insn-00baaca0) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baaca0`](#insn-00baaca0) → [`00baaca4`](#insn-00baaca4)
- ブロック [`00baaca4`](#insn-00baaca4) 範囲 `[['00baaca4', '00baaca7']]`
  - `CONDITIONAL_JUMP` [`00baaca4`](#insn-00baaca4) → [`00baacb8`](#insn-00baacb8)
  - `FALL_THROUGH` [`00baaca4`](#insn-00baaca4) → [`00baaca8`](#insn-00baaca8)
- ブロック [`00baaca8`](#insn-00baaca8) 範囲 `[['00baaca8', '00baacb7']]`
  - `CONDITIONAL_JUMP` [`00baacb4`](#insn-00baacb4) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baacb4`](#insn-00baacb4) → [`00baacb8`](#insn-00baacb8)
- ブロック [`00baacb8`](#insn-00baacb8) 範囲 `[['00baacb8', '00baacbb']]`
  - `CONDITIONAL_JUMP` [`00baacb8`](#insn-00baacb8) → [`00baaccc`](#insn-00baaccc)
  - `FALL_THROUGH` [`00baacb8`](#insn-00baacb8) → [`00baacbc`](#insn-00baacbc)
- ブロック [`00baacbc`](#insn-00baacbc) 範囲 `[['00baacbc', '00baaccb']]`
  - `CONDITIONAL_JUMP` [`00baacc8`](#insn-00baacc8) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baacc8`](#insn-00baacc8) → [`00baaccc`](#insn-00baaccc)
- ブロック [`00baaccc`](#insn-00baaccc) 範囲 `[['00baaccc', '00baaccf']]`
  - `CONDITIONAL_JUMP` [`00baaccc`](#insn-00baaccc) → [`00baace0`](#insn-00baace0)
  - `FALL_THROUGH` [`00baaccc`](#insn-00baaccc) → [`00baacd0`](#insn-00baacd0)
- ブロック [`00baacd0`](#insn-00baacd0) 範囲 `[['00baacd0', '00baacdf']]`
  - `CONDITIONAL_JUMP` [`00baacdc`](#insn-00baacdc) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baacdc`](#insn-00baacdc) → [`00baace0`](#insn-00baace0)
- ブロック [`00baace0`](#insn-00baace0) 範囲 `[['00baace0', '00baace3']]`
  - `CONDITIONAL_JUMP` [`00baace0`](#insn-00baace0) → [`00baacf4`](#insn-00baacf4)
  - `FALL_THROUGH` [`00baace0`](#insn-00baace0) → [`00baace4`](#insn-00baace4)
- ブロック [`00baace4`](#insn-00baace4) 範囲 `[['00baace4', '00baacf3']]`
  - `CONDITIONAL_JUMP` [`00baacf0`](#insn-00baacf0) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baacf0`](#insn-00baacf0) → [`00baacf4`](#insn-00baacf4)
- ブロック [`00baacf4`](#insn-00baacf4) 範囲 `[['00baacf4', '00baacf7']]`
  - `CONDITIONAL_JUMP` [`00baacf4`](#insn-00baacf4) → [`00baad08`](#insn-00baad08)
  - `FALL_THROUGH` [`00baacf4`](#insn-00baacf4) → [`00baacf8`](#insn-00baacf8)
- ブロック [`00baacf8`](#insn-00baacf8) 範囲 `[['00baacf8', '00baad07']]`
  - `CONDITIONAL_JUMP` [`00baad04`](#insn-00baad04) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baad04`](#insn-00baad04) → [`00baad08`](#insn-00baad08)
- ブロック [`00baad08`](#insn-00baad08) 範囲 `[['00baad08', '00baad0b']]`
  - `CONDITIONAL_JUMP` [`00baad08`](#insn-00baad08) → [`00baad1c`](#insn-00baad1c)
  - `FALL_THROUGH` [`00baad08`](#insn-00baad08) → [`00baad0c`](#insn-00baad0c)
- ブロック [`00baad0c`](#insn-00baad0c) 範囲 `[['00baad0c', '00baad1b']]`
  - `CONDITIONAL_JUMP` [`00baad18`](#insn-00baad18) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baad18`](#insn-00baad18) → [`00baad1c`](#insn-00baad1c)
- ブロック [`00baad1c`](#insn-00baad1c) 範囲 `[['00baad1c', '00baad1f']]`
  - `CONDITIONAL_JUMP` [`00baad1c`](#insn-00baad1c) → [`00baad30`](#insn-00baad30)
  - `FALL_THROUGH` [`00baad1c`](#insn-00baad1c) → [`00baad20`](#insn-00baad20)
- ブロック [`00baad20`](#insn-00baad20) 範囲 `[['00baad20', '00baad2f']]`
  - `CONDITIONAL_JUMP` [`00baad2c`](#insn-00baad2c) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baad2c`](#insn-00baad2c) → [`00baad30`](#insn-00baad30)
- ブロック [`00baad30`](#insn-00baad30) 範囲 `[['00baad30', '00baad33']]`
  - `CONDITIONAL_JUMP` [`00baad30`](#insn-00baad30) → [`00baad44`](#insn-00baad44)
  - `FALL_THROUGH` [`00baad30`](#insn-00baad30) → [`00baad34`](#insn-00baad34)
- ブロック [`00baad34`](#insn-00baad34) 範囲 `[['00baad34', '00baad43']]`
  - `CONDITIONAL_JUMP` [`00baad40`](#insn-00baad40) → [`00baad60`](#insn-00baad60)
  - `FALL_THROUGH` [`00baad40`](#insn-00baad40) → [`00baad44`](#insn-00baad44)
- ブロック [`00baad44`](#insn-00baad44) 範囲 `[['00baad44', '00baad47']]`
  - `CONDITIONAL_JUMP` [`00baad44`](#insn-00baad44) → [`00baac80`](#insn-00baac80)
  - `FALL_THROUGH` [`00baad44`](#insn-00baad44) → [`00baad48`](#insn-00baad48)
- ブロック [`00baad48`](#insn-00baad48) 範囲 `[['00baad48', '00baad57']]`
  - `CONDITIONAL_JUMP` [`00baad54`](#insn-00baad54) → [`00baac80`](#insn-00baac80)
  - `FALL_THROUGH` [`00baad54`](#insn-00baad54) → [`00baad58`](#insn-00baad58)
- ブロック [`00baad58`](#insn-00baad58) 範囲 `[['00baad58', '00baad5b']]`
  - `UNCONDITIONAL_JUMP` [`00baad58`](#insn-00baad58) → [`00baad60`](#insn-00baad60)
- ブロック [`00baad5c`](#insn-00baad5c) 範囲 `[['00baad5c', '00baad5f']]`
  - `FALL_THROUGH` [`00baad5c`](#insn-00baad5c) → [`00baad60`](#insn-00baad60)
- ブロック [`00baad60`](#insn-00baad60) 範囲 `[['00baad60', '00baad7b']]`

## 命令位置別の参照

- [`00baac50`](#insn-00baac50) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac54`](#insn-00baac54) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac58`](#insn-00baac58) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac5c`](#insn-00baac5c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac6c`](#insn-00baac6c) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac7c`](#insn-00baac7c) → [`00baac8c`](#insn-00baac8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac88`](#insn-00baac88) → [`00baad5c`](#insn-00baad5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac90`](#insn-00baac90) → [`00baaca4`](#insn-00baaca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac9c`](#insn-00baac9c) → [`00be1950`](../00be1/00be1950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1950` · 推定シンボル `None` · 推定型 `None`
- [`00baaca0`](#insn-00baaca0) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaca4`](#insn-00baaca4) → [`00baacb8`](#insn-00baacb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacb0`](#insn-00baacb0) → [`00be1960`](../00be1/00be1960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1960` · 推定シンボル `None` · 推定型 `None`
- [`00baacb4`](#insn-00baacb4) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacb8`](#insn-00baacb8) → [`00baaccc`](#insn-00baaccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacc4`](#insn-00baacc4) → [`00be1980`](../00be1/00be1980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1980` · 推定シンボル `None` · 推定型 `None`
- [`00baacc8`](#insn-00baacc8) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaccc`](#insn-00baaccc) → [`00baace0`](#insn-00baace0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacd8`](#insn-00baacd8) → [`00be1990`](../00be1/00be1990.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1990` · 推定シンボル `None` · 推定型 `None`
- [`00baacdc`](#insn-00baacdc) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baace0`](#insn-00baace0) → [`00baacf4`](#insn-00baacf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacec`](#insn-00baacec) → [`00be18b0`](../00be1/00be18b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be18b0` · 推定シンボル `None` · 推定型 `None`
- [`00baacf0`](#insn-00baacf0) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacf4`](#insn-00baacf4) → [`00baad08`](#insn-00baad08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad00`](#insn-00baad00) → [`00be19a0`](../00be1/00be19a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19a0` · 推定シンボル `None` · 推定型 `None`
- [`00baad04`](#insn-00baad04) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad08`](#insn-00baad08) → [`00baad1c`](#insn-00baad1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad14`](#insn-00baad14) → [`00be19b0`](../00be1/00be19b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19b0` · 推定シンボル `None` · 推定型 `None`
- [`00baad18`](#insn-00baad18) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad1c`](#insn-00baad1c) → [`00baad30`](#insn-00baad30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad28`](#insn-00baad28) → [`00be19c0`](../00be1/00be19c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19c0` · 推定シンボル `None` · 推定型 `None`
- [`00baad2c`](#insn-00baad2c) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad30`](#insn-00baad30) → [`00baad44`](#insn-00baad44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad3c`](#insn-00baad3c) → [`00be19d0`](../00be1/00be19d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19d0` · 推定シンボル `None` · 推定型 `None`
- [`00baad40`](#insn-00baad40) → [`00baad60`](#insn-00baad60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad44`](#insn-00baad44) → [`00baac80`](#insn-00baac80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad50`](#insn-00baad50) → [`00be1970`](../00be1/00be1970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1970` · 推定シンボル `None` · 推定型 `None`
- [`00baad54`](#insn-00baad54) → [`00baac80`](#insn-00baac80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad58`](#insn-00baad58) → [`00baad60`](#insn-00baad60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad64`](#insn-00baad64) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad68`](#insn-00baad68) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad6c`](#insn-00baad6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad70`](#insn-00baad70) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baac50`](#insn-00baac50)

~~~json
{
  "source": "00baac50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac54`](#insn-00baac54)

~~~json
{
  "source": "00baac54",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac58`](#insn-00baac58)

~~~json
{
  "source": "00baac58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac5c`](#insn-00baac5c)

~~~json
{
  "source": "00baac5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac6c`](#insn-00baac6c)

~~~json
{
  "source": "00baac6c",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac7c`](#insn-00baac7c)

~~~json
{
  "source": "00baac7c",
  "target": "00baac8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac88`](#insn-00baac88)

~~~json
{
  "source": "00baac88",
  "target": "00baad5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac90`](#insn-00baac90)

~~~json
{
  "source": "00baac90",
  "target": "00baaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac9c`](#insn-00baac9c)

~~~json
{
  "source": "00baac9c",
  "target": "00be1950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baaca0`](#insn-00baaca0)

~~~json
{
  "source": "00baaca0",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaca4`](#insn-00baaca4)

~~~json
{
  "source": "00baaca4",
  "target": "00baacb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacb0`](#insn-00baacb0)

~~~json
{
  "source": "00baacb0",
  "target": "00be1960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baacb4`](#insn-00baacb4)

~~~json
{
  "source": "00baacb4",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacb8`](#insn-00baacb8)

~~~json
{
  "source": "00baacb8",
  "target": "00baaccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacc4`](#insn-00baacc4)

~~~json
{
  "source": "00baacc4",
  "target": "00be1980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baacc8`](#insn-00baacc8)

~~~json
{
  "source": "00baacc8",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaccc`](#insn-00baaccc)

~~~json
{
  "source": "00baaccc",
  "target": "00baace0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacd8`](#insn-00baacd8)

~~~json
{
  "source": "00baacd8",
  "target": "00be1990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baacdc`](#insn-00baacdc)

~~~json
{
  "source": "00baacdc",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baace0`](#insn-00baace0)

~~~json
{
  "source": "00baace0",
  "target": "00baacf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacec`](#insn-00baacec)

~~~json
{
  "source": "00baacec",
  "target": "00be18b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baacf0`](#insn-00baacf0)

~~~json
{
  "source": "00baacf0",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacf4`](#insn-00baacf4)

~~~json
{
  "source": "00baacf4",
  "target": "00baad08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad00`](#insn-00baad00)

~~~json
{
  "source": "00baad00",
  "target": "00be19a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad04`](#insn-00baad04)

~~~json
{
  "source": "00baad04",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad08`](#insn-00baad08)

~~~json
{
  "source": "00baad08",
  "target": "00baad1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad14`](#insn-00baad14)

~~~json
{
  "source": "00baad14",
  "target": "00be19b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad18`](#insn-00baad18)

~~~json
{
  "source": "00baad18",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad1c`](#insn-00baad1c)

~~~json
{
  "source": "00baad1c",
  "target": "00baad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad28`](#insn-00baad28)

~~~json
{
  "source": "00baad28",
  "target": "00be19c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad2c`](#insn-00baad2c)

~~~json
{
  "source": "00baad2c",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad30`](#insn-00baad30)

~~~json
{
  "source": "00baad30",
  "target": "00baad44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad3c`](#insn-00baad3c)

~~~json
{
  "source": "00baad3c",
  "target": "00be19d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad40`](#insn-00baad40)

~~~json
{
  "source": "00baad40",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad44`](#insn-00baad44)

~~~json
{
  "source": "00baad44",
  "target": "00baac80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad50`](#insn-00baad50)

~~~json
{
  "source": "00baad50",
  "target": "00be1970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad54`](#insn-00baad54)

~~~json
{
  "source": "00baad54",
  "target": "00baac80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad58`](#insn-00baad58)

~~~json
{
  "source": "00baad58",
  "target": "00baad60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad64`](#insn-00baad64)

~~~json
{
  "source": "00baad64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad68`](#insn-00baad68)

~~~json
{
  "source": "00baad68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad6c`](#insn-00baad6c)

~~~json
{
  "source": "00baad6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad70`](#insn-00baad70)

~~~json
{
  "source": "00baad70",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
