# 00baad7c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baae44`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baae44.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-de5e55ed9e8966b3561ded348b6b08d5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baad7c",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE11do_scan_notEmPKwS3_",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1ff1555b2d0e6bdbf31263f14273c38637eab87cbcc102862f2f52f8b387ed85",
  "source_text_sha256": "1ff1555b2d0e6bdbf31263f14273c38637eab87cbcc102862f2f52f8b387ed85",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baad7c",
        "00baaeab"
      ]
    ],
    "bytes_sha256": "05e603fd0b3d0ed14ac4140276227637eed78caf810ea0486de391ffb9f3f406",
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

## 疑似コード / UTF-8 1671 bytes

~~~c

wint_t * _ZNKSt6__ndk112ctype_bynameIwE11do_scan_notEmPKwS3_
                   (long param_1,uint param_2,wint_t *param_3,wint_t *param_4)

{
  wint_t __wc;
  int iVar1;
  wint_t *pwVar2;
  
  pwVar2 = param_3;
  while ((param_3 != param_4 &&
         (((((__wc = *param_3, (param_2 & 1) != 0 &&
             (iVar1 = iswspace_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
            (((param_2 >> 1 & 1) != 0 &&
             (iVar1 = iswprint_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)))) ||
           (((((param_2 >> 2 & 1) != 0 &&
              (iVar1 = iswcntrl_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
             (((param_2 >> 3 & 1) != 0 &&
              (iVar1 = iswupper_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)))) ||
            (((((param_2 >> 4 & 1) != 0 &&
               (iVar1 = iswlower_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
              (((param_2 >> 5 & 1) != 0 &&
               (iVar1 = iswalpha_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)))) ||
             (((param_2 >> 6 & 1) != 0 &&
              (iVar1 = iswdigit_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)))))))) ||
          ((((param_2 >> 7 & 1) != 0 &&
            (iVar1 = iswpunct_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
           ((((param_2 >> 8 & 1) != 0 &&
             (iVar1 = iswxdigit_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0)) ||
            ((pwVar2 = param_3, (param_2 >> 9 & 1) != 0 &&
             (iVar1 = iswblank_l(__wc,*(__locale_t *)(param_1 + 0x10)), iVar1 != 0))))))))))) {
    param_3 = param_3 + 1;
    pwVar2 = param_4;
  }
  return pwVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baad7c"></a> `00baad7c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baad80"></a> `00baad80` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baad84"></a> `00baad84` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baad88"></a> `00baad88` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baad8c"></a> `00baad8c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baad90"></a> `00baad90` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baad94"></a> `00baad94` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00baad98"></a> `00baad98` | `5f 00 03 eb` | cmp x2,x3 | `FALL_THROUGH`
<a id="insn-00baad9c"></a> `00baad9c` | `a0 07 00 54` | b.eq 0x00baae90 | `CONDITIONAL_JUMP`
<a id="insn-00baada0"></a> `00baada0` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00baada4"></a> `00baada4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00baada8"></a> `00baada8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00baadac"></a> `00baadac` | `08 00 00 14` | b 0x00baadcc | `UNCONDITIONAL_JUMP`
<a id="insn-00baadb0"></a> `00baadb0` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baadb4"></a> `00baadb4` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baadb8"></a> `00baadb8` | `e6 da 00 94` | bl 0x00be1950 | `UNCONDITIONAL_CALL`
<a id="insn-00baadbc"></a> `00baadbc` | `c0 00 00 34` | cbz w0,0x00baadd4 | `CONDITIONAL_JUMP`
<a id="insn-00baadc0"></a> `00baadc0` | `73 12 00 91` | add x19,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00baadc4"></a> `00baadc4` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00baadc8"></a> `00baadc8` | `20 06 00 54` | b.eq 0x00baae8c | `CONDITIONAL_JUMP`
<a id="insn-00baadcc"></a> `00baadcc` | `77 02 40 b9` | ldr w23,[x19] | `FALL_THROUGH`
<a id="insn-00baadd0"></a> `00baadd0` | `15 ff 07 37` | tbnz w21,#0x0,0x00baadb0 | `CONDITIONAL_JUMP`
<a id="insn-00baadd4"></a> `00baadd4` | `b5 00 08 36` | tbz w21,#0x1,0x00baade8 | `CONDITIONAL_JUMP`
<a id="insn-00baadd8"></a> `00baadd8` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baaddc"></a> `00baaddc` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baade0"></a> `00baade0` | `e0 da 00 94` | bl 0x00be1960 | `UNCONDITIONAL_CALL`
<a id="insn-00baade4"></a> `00baade4` | `e0 fe ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baade8"></a> `00baade8` | `b5 00 10 36` | tbz w21,#0x2,0x00baadfc | `CONDITIONAL_JUMP`
<a id="insn-00baadec"></a> `00baadec` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baadf0"></a> `00baadf0` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baadf4"></a> `00baadf4` | `e3 da 00 94` | bl 0x00be1980 | `UNCONDITIONAL_CALL`
<a id="insn-00baadf8"></a> `00baadf8` | `40 fe ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baadfc"></a> `00baadfc` | `b5 00 18 36` | tbz w21,#0x3,0x00baae10 | `CONDITIONAL_JUMP`
<a id="insn-00baae00"></a> `00baae00` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baae04"></a> `00baae04` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baae08"></a> `00baae08` | `e2 da 00 94` | bl 0x00be1990 | `UNCONDITIONAL_CALL`
<a id="insn-00baae0c"></a> `00baae0c` | `a0 fd ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baae10"></a> `00baae10` | `b5 00 20 36` | tbz w21,#0x4,0x00baae24 | `CONDITIONAL_JUMP`
<a id="insn-00baae14"></a> `00baae14` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baae18"></a> `00baae18` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baae1c"></a> `00baae1c` | `a5 da 00 94` | bl 0x00be18b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baae20"></a> `00baae20` | `00 fd ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baae24"></a> `00baae24` | `b5 00 28 36` | tbz w21,#0x5,0x00baae38 | `CONDITIONAL_JUMP`
<a id="insn-00baae28"></a> `00baae28` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baae2c"></a> `00baae2c` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baae30"></a> `00baae30` | `dc da 00 94` | bl 0x00be19a0 | `UNCONDITIONAL_CALL`
<a id="insn-00baae34"></a> `00baae34` | `60 fc ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baae38"></a> `00baae38` | `b5 00 30 36` | tbz w21,#0x6,0x00baae4c | `CONDITIONAL_JUMP`
<a id="insn-00baae3c"></a> `00baae3c` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baae40"></a> `00baae40` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baae44"></a> `00baae44` | `db da 00 94` | bl 0x00be19b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baae48"></a> `00baae48` | `c0 fb ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baae4c"></a> `00baae4c` | `b5 00 38 36` | tbz w21,#0x7,0x00baae60 | `CONDITIONAL_JUMP`
<a id="insn-00baae50"></a> `00baae50` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baae54"></a> `00baae54` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baae58"></a> `00baae58` | `da da 00 94` | bl 0x00be19c0 | `UNCONDITIONAL_CALL`
<a id="insn-00baae5c"></a> `00baae5c` | `20 fb ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baae60"></a> `00baae60` | `b5 00 40 36` | tbz w21,#0x8,0x00baae74 | `CONDITIONAL_JUMP`
<a id="insn-00baae64"></a> `00baae64` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baae68"></a> `00baae68` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baae6c"></a> `00baae6c` | `d9 da 00 94` | bl 0x00be19d0 | `UNCONDITIONAL_CALL`
<a id="insn-00baae70"></a> `00baae70` | `80 fa ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baae74"></a> `00baae74` | `f5 00 48 36` | tbz w21,#0x9,0x00baae90 | `CONDITIONAL_JUMP`
<a id="insn-00baae78"></a> `00baae78` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baae7c"></a> `00baae7c` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baae80"></a> `00baae80` | `bc da 00 94` | bl 0x00be1970 | `UNCONDITIONAL_CALL`
<a id="insn-00baae84"></a> `00baae84` | `e0 f9 ff 35` | cbnz w0,0x00baadc0 | `CONDITIONAL_JUMP`
<a id="insn-00baae88"></a> `00baae88` | `02 00 00 14` | b 0x00baae90 | `UNCONDITIONAL_JUMP`
<a id="insn-00baae8c"></a> `00baae8c` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00baae90"></a> `00baae90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baae94"></a> `00baae94` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baae98"></a> `00baae98` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baae9c"></a> `00baae9c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaea0"></a> `00baaea0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baaea4"></a> `00baaea4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baaea8"></a> `00baaea8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baad7c`](#insn-00baad7c) 範囲 `[['00baad7c', '00baad9f']]`
  - `CONDITIONAL_JUMP` [`00baad9c`](#insn-00baad9c) → [`00baae90`](#insn-00baae90)
  - `FALL_THROUGH` [`00baad9c`](#insn-00baad9c) → [`00baada0`](#insn-00baada0)
- ブロック [`00baada0`](#insn-00baada0) 範囲 `[['00baada0', '00baadaf']]`
  - `UNCONDITIONAL_JUMP` [`00baadac`](#insn-00baadac) → [`00baadcc`](#insn-00baadcc)
- ブロック [`00baadb0`](#insn-00baadb0) 範囲 `[['00baadb0', '00baadbf']]`
  - `CONDITIONAL_JUMP` [`00baadbc`](#insn-00baadbc) → [`00baadd4`](#insn-00baadd4)
  - `FALL_THROUGH` [`00baadbc`](#insn-00baadbc) → [`00baadc0`](#insn-00baadc0)
- ブロック [`00baadc0`](#insn-00baadc0) 範囲 `[['00baadc0', '00baadcb']]`
  - `CONDITIONAL_JUMP` [`00baadc8`](#insn-00baadc8) → [`00baae8c`](#insn-00baae8c)
  - `FALL_THROUGH` [`00baadc8`](#insn-00baadc8) → [`00baadcc`](#insn-00baadcc)
- ブロック [`00baadcc`](#insn-00baadcc) 範囲 `[['00baadcc', '00baadd3']]`
  - `CONDITIONAL_JUMP` [`00baadd0`](#insn-00baadd0) → [`00baadb0`](#insn-00baadb0)
  - `FALL_THROUGH` [`00baadd0`](#insn-00baadd0) → [`00baadd4`](#insn-00baadd4)
- ブロック [`00baadd4`](#insn-00baadd4) 範囲 `[['00baadd4', '00baadd7']]`
  - `CONDITIONAL_JUMP` [`00baadd4`](#insn-00baadd4) → [`00baade8`](#insn-00baade8)
  - `FALL_THROUGH` [`00baadd4`](#insn-00baadd4) → [`00baadd8`](#insn-00baadd8)
- ブロック [`00baadd8`](#insn-00baadd8) 範囲 `[['00baadd8', '00baade7']]`
  - `CONDITIONAL_JUMP` [`00baade4`](#insn-00baade4) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baade4`](#insn-00baade4) → [`00baade8`](#insn-00baade8)
- ブロック [`00baade8`](#insn-00baade8) 範囲 `[['00baade8', '00baadeb']]`
  - `CONDITIONAL_JUMP` [`00baade8`](#insn-00baade8) → [`00baadfc`](#insn-00baadfc)
  - `FALL_THROUGH` [`00baade8`](#insn-00baade8) → [`00baadec`](#insn-00baadec)
- ブロック [`00baadec`](#insn-00baadec) 範囲 `[['00baadec', '00baadfb']]`
  - `CONDITIONAL_JUMP` [`00baadf8`](#insn-00baadf8) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baadf8`](#insn-00baadf8) → [`00baadfc`](#insn-00baadfc)
- ブロック [`00baadfc`](#insn-00baadfc) 範囲 `[['00baadfc', '00baadff']]`
  - `CONDITIONAL_JUMP` [`00baadfc`](#insn-00baadfc) → [`00baae10`](#insn-00baae10)
  - `FALL_THROUGH` [`00baadfc`](#insn-00baadfc) → [`00baae00`](#insn-00baae00)
- ブロック [`00baae00`](#insn-00baae00) 範囲 `[['00baae00', '00baae0f']]`
  - `CONDITIONAL_JUMP` [`00baae0c`](#insn-00baae0c) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baae0c`](#insn-00baae0c) → [`00baae10`](#insn-00baae10)
- ブロック [`00baae10`](#insn-00baae10) 範囲 `[['00baae10', '00baae13']]`
  - `CONDITIONAL_JUMP` [`00baae10`](#insn-00baae10) → [`00baae24`](#insn-00baae24)
  - `FALL_THROUGH` [`00baae10`](#insn-00baae10) → [`00baae14`](#insn-00baae14)
- ブロック [`00baae14`](#insn-00baae14) 範囲 `[['00baae14', '00baae23']]`
  - `CONDITIONAL_JUMP` [`00baae20`](#insn-00baae20) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baae20`](#insn-00baae20) → [`00baae24`](#insn-00baae24)
- ブロック [`00baae24`](#insn-00baae24) 範囲 `[['00baae24', '00baae27']]`
  - `CONDITIONAL_JUMP` [`00baae24`](#insn-00baae24) → [`00baae38`](#insn-00baae38)
  - `FALL_THROUGH` [`00baae24`](#insn-00baae24) → [`00baae28`](#insn-00baae28)
- ブロック [`00baae28`](#insn-00baae28) 範囲 `[['00baae28', '00baae37']]`
  - `CONDITIONAL_JUMP` [`00baae34`](#insn-00baae34) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baae34`](#insn-00baae34) → [`00baae38`](#insn-00baae38)
- ブロック [`00baae38`](#insn-00baae38) 範囲 `[['00baae38', '00baae3b']]`
  - `CONDITIONAL_JUMP` [`00baae38`](#insn-00baae38) → [`00baae4c`](#insn-00baae4c)
  - `FALL_THROUGH` [`00baae38`](#insn-00baae38) → [`00baae3c`](#insn-00baae3c)
- ブロック [`00baae3c`](#insn-00baae3c) 範囲 `[['00baae3c', '00baae4b']]`
  - `CONDITIONAL_JUMP` [`00baae48`](#insn-00baae48) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baae48`](#insn-00baae48) → [`00baae4c`](#insn-00baae4c)
- ブロック [`00baae4c`](#insn-00baae4c) 範囲 `[['00baae4c', '00baae4f']]`
  - `CONDITIONAL_JUMP` [`00baae4c`](#insn-00baae4c) → [`00baae60`](#insn-00baae60)
  - `FALL_THROUGH` [`00baae4c`](#insn-00baae4c) → [`00baae50`](#insn-00baae50)
- ブロック [`00baae50`](#insn-00baae50) 範囲 `[['00baae50', '00baae5f']]`
  - `CONDITIONAL_JUMP` [`00baae5c`](#insn-00baae5c) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baae5c`](#insn-00baae5c) → [`00baae60`](#insn-00baae60)
- ブロック [`00baae60`](#insn-00baae60) 範囲 `[['00baae60', '00baae63']]`
  - `CONDITIONAL_JUMP` [`00baae60`](#insn-00baae60) → [`00baae74`](#insn-00baae74)
  - `FALL_THROUGH` [`00baae60`](#insn-00baae60) → [`00baae64`](#insn-00baae64)
- ブロック [`00baae64`](#insn-00baae64) 範囲 `[['00baae64', '00baae73']]`
  - `CONDITIONAL_JUMP` [`00baae70`](#insn-00baae70) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baae70`](#insn-00baae70) → [`00baae74`](#insn-00baae74)
- ブロック [`00baae74`](#insn-00baae74) 範囲 `[['00baae74', '00baae77']]`
  - `CONDITIONAL_JUMP` [`00baae74`](#insn-00baae74) → [`00baae90`](#insn-00baae90)
  - `FALL_THROUGH` [`00baae74`](#insn-00baae74) → [`00baae78`](#insn-00baae78)
- ブロック [`00baae78`](#insn-00baae78) 範囲 `[['00baae78', '00baae87']]`
  - `CONDITIONAL_JUMP` [`00baae84`](#insn-00baae84) → [`00baadc0`](#insn-00baadc0)
  - `FALL_THROUGH` [`00baae84`](#insn-00baae84) → [`00baae88`](#insn-00baae88)
- ブロック [`00baae88`](#insn-00baae88) 範囲 `[['00baae88', '00baae8b']]`
  - `UNCONDITIONAL_JUMP` [`00baae88`](#insn-00baae88) → [`00baae90`](#insn-00baae90)
- ブロック [`00baae8c`](#insn-00baae8c) 範囲 `[['00baae8c', '00baae8f']]`
  - `FALL_THROUGH` [`00baae8c`](#insn-00baae8c) → [`00baae90`](#insn-00baae90)
- ブロック [`00baae90`](#insn-00baae90) 範囲 `[['00baae90', '00baaeab']]`

## 命令位置別の参照

- [`00baad80`](#insn-00baad80) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad84`](#insn-00baad84) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad88`](#insn-00baad88) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad8c`](#insn-00baad8c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad9c`](#insn-00baad9c) → [`00baae90`](#insn-00baae90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadac`](#insn-00baadac) → [`00baadcc`](#insn-00baadcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadb8`](#insn-00baadb8) → [`00be1950`](../00be1/00be1950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1950` · 推定シンボル `None` · 推定型 `None`
- [`00baadbc`](#insn-00baadbc) → [`00baadd4`](#insn-00baadd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadc8`](#insn-00baadc8) → [`00baae8c`](#insn-00baae8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd0`](#insn-00baadd0) → [`00baadb0`](#insn-00baadb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadd4`](#insn-00baadd4) → [`00baade8`](#insn-00baade8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baade0`](#insn-00baade0) → [`00be1960`](../00be1/00be1960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1960` · 推定シンボル `None` · 推定型 `None`
- [`00baade4`](#insn-00baade4) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baade8`](#insn-00baade8) → [`00baadfc`](#insn-00baadfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadf4`](#insn-00baadf4) → [`00be1980`](../00be1/00be1980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1980` · 推定シンボル `None` · 推定型 `None`
- [`00baadf8`](#insn-00baadf8) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baadfc`](#insn-00baadfc) → [`00baae10`](#insn-00baae10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae08`](#insn-00baae08) → [`00be1990`](../00be1/00be1990.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1990` · 推定シンボル `None` · 推定型 `None`
- [`00baae0c`](#insn-00baae0c) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae10`](#insn-00baae10) → [`00baae24`](#insn-00baae24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae1c`](#insn-00baae1c) → [`00be18b0`](../00be1/00be18b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be18b0` · 推定シンボル `None` · 推定型 `None`
- [`00baae20`](#insn-00baae20) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae24`](#insn-00baae24) → [`00baae38`](#insn-00baae38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae30`](#insn-00baae30) → [`00be19a0`](../00be1/00be19a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19a0` · 推定シンボル `None` · 推定型 `None`
- [`00baae34`](#insn-00baae34) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae38`](#insn-00baae38) → [`00baae4c`](#insn-00baae4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae44`](#insn-00baae44) → [`00be19b0`](../00be1/00be19b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19b0` · 推定シンボル `None` · 推定型 `None`
- [`00baae48`](#insn-00baae48) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae4c`](#insn-00baae4c) → [`00baae60`](#insn-00baae60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae58`](#insn-00baae58) → [`00be19c0`](../00be1/00be19c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19c0` · 推定シンボル `None` · 推定型 `None`
- [`00baae5c`](#insn-00baae5c) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae60`](#insn-00baae60) → [`00baae74`](#insn-00baae74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae6c`](#insn-00baae6c) → [`00be19d0`](../00be1/00be19d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19d0` · 推定シンボル `None` · 推定型 `None`
- [`00baae70`](#insn-00baae70) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae74`](#insn-00baae74) → [`00baae90`](#insn-00baae90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae80`](#insn-00baae80) → [`00be1970`](../00be1/00be1970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1970` · 推定シンボル `None` · 推定型 `None`
- [`00baae84`](#insn-00baae84) → [`00baadc0`](#insn-00baadc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae88`](#insn-00baae88) → [`00baae90`](#insn-00baae90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae94`](#insn-00baae94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae98`](#insn-00baae98) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baae9c`](#insn-00baae9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaea0`](#insn-00baaea0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baad80`](#insn-00baad80)

~~~json
{
  "source": "00baad80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad84`](#insn-00baad84)

~~~json
{
  "source": "00baad84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad88`](#insn-00baad88)

~~~json
{
  "source": "00baad88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad8c`](#insn-00baad8c)

~~~json
{
  "source": "00baad8c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad9c`](#insn-00baad9c)

~~~json
{
  "source": "00baad9c",
  "target": "00baae90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadac`](#insn-00baadac)

~~~json
{
  "source": "00baadac",
  "target": "00baadcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadb8`](#insn-00baadb8)

~~~json
{
  "source": "00baadb8",
  "target": "00be1950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baadbc`](#insn-00baadbc)

~~~json
{
  "source": "00baadbc",
  "target": "00baadd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadc8`](#insn-00baadc8)

~~~json
{
  "source": "00baadc8",
  "target": "00baae8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd0`](#insn-00baadd0)

~~~json
{
  "source": "00baadd0",
  "target": "00baadb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadd4`](#insn-00baadd4)

~~~json
{
  "source": "00baadd4",
  "target": "00baade8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baade0`](#insn-00baade0)

~~~json
{
  "source": "00baade0",
  "target": "00be1960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baade4`](#insn-00baade4)

~~~json
{
  "source": "00baade4",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baade8`](#insn-00baade8)

~~~json
{
  "source": "00baade8",
  "target": "00baadfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadf4`](#insn-00baadf4)

~~~json
{
  "source": "00baadf4",
  "target": "00be1980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baadf8`](#insn-00baadf8)

~~~json
{
  "source": "00baadf8",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baadfc`](#insn-00baadfc)

~~~json
{
  "source": "00baadfc",
  "target": "00baae10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae08`](#insn-00baae08)

~~~json
{
  "source": "00baae08",
  "target": "00be1990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae0c`](#insn-00baae0c)

~~~json
{
  "source": "00baae0c",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae10`](#insn-00baae10)

~~~json
{
  "source": "00baae10",
  "target": "00baae24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae1c`](#insn-00baae1c)

~~~json
{
  "source": "00baae1c",
  "target": "00be18b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae20`](#insn-00baae20)

~~~json
{
  "source": "00baae20",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae24`](#insn-00baae24)

~~~json
{
  "source": "00baae24",
  "target": "00baae38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae30`](#insn-00baae30)

~~~json
{
  "source": "00baae30",
  "target": "00be19a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae34`](#insn-00baae34)

~~~json
{
  "source": "00baae34",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae38`](#insn-00baae38)

~~~json
{
  "source": "00baae38",
  "target": "00baae4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae44`](#insn-00baae44)

~~~json
{
  "source": "00baae44",
  "target": "00be19b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae48`](#insn-00baae48)

~~~json
{
  "source": "00baae48",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae4c`](#insn-00baae4c)

~~~json
{
  "source": "00baae4c",
  "target": "00baae60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae58`](#insn-00baae58)

~~~json
{
  "source": "00baae58",
  "target": "00be19c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae5c`](#insn-00baae5c)

~~~json
{
  "source": "00baae5c",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae60`](#insn-00baae60)

~~~json
{
  "source": "00baae60",
  "target": "00baae74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae6c`](#insn-00baae6c)

~~~json
{
  "source": "00baae6c",
  "target": "00be19d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae70`](#insn-00baae70)

~~~json
{
  "source": "00baae70",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae74`](#insn-00baae74)

~~~json
{
  "source": "00baae74",
  "target": "00baae90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae80`](#insn-00baae80)

~~~json
{
  "source": "00baae80",
  "target": "00be1970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baae84`](#insn-00baae84)

~~~json
{
  "source": "00baae84",
  "target": "00baadc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae88`](#insn-00baae88)

~~~json
{
  "source": "00baae88",
  "target": "00baae90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae94`](#insn-00baae94)

~~~json
{
  "source": "00baae94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae98`](#insn-00baae98)

~~~json
{
  "source": "00baae98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baae9c`](#insn-00baae9c)

~~~json
{
  "source": "00baae9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaea0`](#insn-00baaea0)

~~~json
{
  "source": "00baaea0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
