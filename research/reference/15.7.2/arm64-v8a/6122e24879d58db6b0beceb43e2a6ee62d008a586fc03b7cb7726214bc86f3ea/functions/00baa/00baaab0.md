# 00baaab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baab78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0005.md#compare-1dcc2a1e0248d9c865c10e5c3bb4280e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaab0",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE5do_isEPKwS3_Pm",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c15fb5a32a1181b30a46ed4089f889256ee6d61994fe526164e718937eb2708",
  "source_text_sha256": "7c15fb5a32a1181b30a46ed4089f889256ee6d61994fe526164e718937eb2708",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaab0",
        "00baac4b"
      ]
    ],
    "bytes_sha256": "5218bf5a0af023f60055c1b8174520ab4c4fcdba4326393b5d7f5a2ef2ad2403",
    "instruction_count": 103,
    "instruction_bytes": 412,
    "body_bytes": 412,
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

## 疑似コード / UTF-8 1943 bytes

~~~c

uint * _ZNKSt6__ndk112ctype_bynameIwE5do_isEPKwS3_Pm
                 (long param_1,uint *param_2,uint *param_3,ulong *param_4)

{
  uint __wc;
  uint *puVar1;
  int iVar2;
  __locale_t __locale;
  ulong uVar3;
  
  puVar1 = param_2;
  do {
    if (param_2 == param_3) {
      return puVar1;
    }
    __wc = *param_2;
    if (__wc < 0x80) {
      uVar3 = *(ulong *)(&DAT_002fb120 + (ulong)__wc * 8);
LAB_00baaaf0:
      *param_4 = uVar3;
    }
    else {
      __locale = *(__locale_t *)(param_1 + 0x10);
      *param_4 = 0;
      iVar2 = iswspace_l(__wc,__locale);
      if (iVar2 != 0) {
        *param_4 = *param_4 | 1;
      }
      iVar2 = iswprint_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 2;
      }
      iVar2 = iswcntrl_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 4;
      }
      iVar2 = iswupper_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 8;
      }
      iVar2 = iswlower_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x10;
      }
      iVar2 = iswalpha_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x20;
      }
      iVar2 = iswdigit_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x40;
      }
      iVar2 = iswpunct_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x80;
      }
      iVar2 = iswxdigit_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        *param_4 = *param_4 | 0x100;
      }
      iVar2 = iswblank_l(__wc,*(__locale_t *)(param_1 + 0x10));
      if (iVar2 != 0) {
        uVar3 = *param_4 | 0x200;
        goto LAB_00baaaf0;
      }
    }
    param_2 = param_2 + 1;
    param_4 = param_4 + 1;
    puVar1 = param_3;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baaab0"></a> `00baaab0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baaab4"></a> `00baaab4` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baaab8"></a> `00baaab8` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baaabc"></a> `00baaabc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baaac0"></a> `00baaac0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baaac4"></a> `00baaac4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baaac8"></a> `00baaac8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baaacc"></a> `00baaacc` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00baaad0"></a> `00baaad0` | `00 0b 00 54` | b.eq 0x00baac30 | `CONDITIONAL_JUMP`
<a id="insn-00baaad4"></a> `00baaad4` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00baaad8"></a> `00baaad8` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00baaadc"></a> `00baaadc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00baaae0"></a> `00baaae0` | `98 ba ff b0` | adrp x24,0x2fb000 | `FALL_THROUGH`
<a id="insn-00baaae4"></a> `00baaae4` | `18 83 04 91` | add x24,x24,#0x120 | `FALL_THROUGH`
<a id="insn-00baaae8"></a> `00baaae8` | `07 00 00 14` | b 0x00baab04 | `UNCONDITIONAL_JUMP`
<a id="insn-00baaaec"></a> `00baaaec` | `08 7b 77 f8` | ldr x8,[x24, x23, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00baaaf0"></a> `00baaaf0` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baaaf4"></a> `00baaaf4` | `73 12 00 91` | add x19,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00baaaf8"></a> `00baaaf8` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00baaafc"></a> `00baaafc` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00baab00"></a> `00baab00` | `60 09 00 54` | b.eq 0x00baac2c | `CONDITIONAL_JUMP`
<a id="insn-00baab04"></a> `00baab04` | `77 02 40 b9` | ldr w23,[x19] | `FALL_THROUGH`
<a id="insn-00baab08"></a> `00baab08` | `ff fe 01 71` | cmp w23,#0x7f | `FALL_THROUGH`
<a id="insn-00baab0c"></a> `00baab0c` | `09 ff ff 54` | b.ls 0x00baaaec | `CONDITIONAL_JUMP`
<a id="insn-00baab10"></a> `00baab10` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baab14"></a> `00baab14` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baab18"></a> `00baab18` | `bf 02 00 f9` | str xzr,[x21] | `FALL_THROUGH`
<a id="insn-00baab1c"></a> `00baab1c` | `8d db 00 94` | bl 0x00be1950 | `UNCONDITIONAL_CALL`
<a id="insn-00baab20"></a> `00baab20` | `80 00 00 34` | cbz w0,0x00baab30 | `CONDITIONAL_JUMP`
<a id="insn-00baab24"></a> `00baab24` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab28"></a> `00baab28` | `08 01 40 b2` | orr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baab2c"></a> `00baab2c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab30"></a> `00baab30` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baab34"></a> `00baab34` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baab38"></a> `00baab38` | `8a db 00 94` | bl 0x00be1960 | `UNCONDITIONAL_CALL`
<a id="insn-00baab3c"></a> `00baab3c` | `80 00 00 34` | cbz w0,0x00baab4c | `CONDITIONAL_JUMP`
<a id="insn-00baab40"></a> `00baab40` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab44"></a> `00baab44` | `08 01 7f b2` | orr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00baab48"></a> `00baab48` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab4c"></a> `00baab4c` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baab50"></a> `00baab50` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baab54"></a> `00baab54` | `8b db 00 94` | bl 0x00be1980 | `UNCONDITIONAL_CALL`
<a id="insn-00baab58"></a> `00baab58` | `80 00 00 34` | cbz w0,0x00baab68 | `CONDITIONAL_JUMP`
<a id="insn-00baab5c"></a> `00baab5c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab60"></a> `00baab60` | `08 01 7e b2` | orr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00baab64"></a> `00baab64` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab68"></a> `00baab68` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baab6c"></a> `00baab6c` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baab70"></a> `00baab70` | `88 db 00 94` | bl 0x00be1990 | `UNCONDITIONAL_CALL`
<a id="insn-00baab74"></a> `00baab74` | `80 00 00 34` | cbz w0,0x00baab84 | `CONDITIONAL_JUMP`
<a id="insn-00baab78"></a> `00baab78` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab7c"></a> `00baab7c` | `08 01 7d b2` | orr x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00baab80"></a> `00baab80` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab84"></a> `00baab84` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baab88"></a> `00baab88` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baab8c"></a> `00baab8c` | `49 db 00 94` | bl 0x00be18b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baab90"></a> `00baab90` | `80 00 00 34` | cbz w0,0x00baaba0 | `CONDITIONAL_JUMP`
<a id="insn-00baab94"></a> `00baab94` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baab98"></a> `00baab98` | `08 01 7c b2` | orr x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00baab9c"></a> `00baab9c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baaba0"></a> `00baaba0` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baaba4"></a> `00baaba4` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baaba8"></a> `00baaba8` | `7e db 00 94` | bl 0x00be19a0 | `UNCONDITIONAL_CALL`
<a id="insn-00baabac"></a> `00baabac` | `80 00 00 34` | cbz w0,0x00baabbc | `CONDITIONAL_JUMP`
<a id="insn-00baabb0"></a> `00baabb0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baabb4"></a> `00baabb4` | `08 01 7b b2` | orr x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00baabb8"></a> `00baabb8` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baabbc"></a> `00baabbc` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baabc0"></a> `00baabc0` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baabc4"></a> `00baabc4` | `7b db 00 94` | bl 0x00be19b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baabc8"></a> `00baabc8` | `80 00 00 34` | cbz w0,0x00baabd8 | `CONDITIONAL_JUMP`
<a id="insn-00baabcc"></a> `00baabcc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baabd0"></a> `00baabd0` | `08 01 7a b2` | orr x8,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00baabd4"></a> `00baabd4` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baabd8"></a> `00baabd8` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baabdc"></a> `00baabdc` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baabe0"></a> `00baabe0` | `78 db 00 94` | bl 0x00be19c0 | `UNCONDITIONAL_CALL`
<a id="insn-00baabe4"></a> `00baabe4` | `80 00 00 34` | cbz w0,0x00baabf4 | `CONDITIONAL_JUMP`
<a id="insn-00baabe8"></a> `00baabe8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baabec"></a> `00baabec` | `08 01 79 b2` | orr x8,x8,#0x80 | `FALL_THROUGH`
<a id="insn-00baabf0"></a> `00baabf0` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baabf4"></a> `00baabf4` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baabf8"></a> `00baabf8` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baabfc"></a> `00baabfc` | `75 db 00 94` | bl 0x00be19d0 | `UNCONDITIONAL_CALL`
<a id="insn-00baac00"></a> `00baac00` | `80 00 00 34` | cbz w0,0x00baac10 | `CONDITIONAL_JUMP`
<a id="insn-00baac04"></a> `00baac04` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac08"></a> `00baac08` | `08 01 78 b2` | orr x8,x8,#0x100 | `FALL_THROUGH`
<a id="insn-00baac0c"></a> `00baac0c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac10"></a> `00baac10` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baac14"></a> `00baac14` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baac18"></a> `00baac18` | `56 db 00 94` | bl 0x00be1970 | `UNCONDITIONAL_CALL`
<a id="insn-00baac1c"></a> `00baac1c` | `c0 f6 ff 34` | cbz w0,0x00baaaf4 | `CONDITIONAL_JUMP`
<a id="insn-00baac20"></a> `00baac20` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac24"></a> `00baac24` | `08 01 77 b2` | orr x8,x8,#0x200 | `FALL_THROUGH`
<a id="insn-00baac28"></a> `00baac28` | `b2 ff ff 17` | b 0x00baaaf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00baac2c"></a> `00baac2c` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00baac30"></a> `00baac30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baac34"></a> `00baac34` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baac38"></a> `00baac38` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baac3c"></a> `00baac3c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baac40"></a> `00baac40` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baac44"></a> `00baac44` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baac48"></a> `00baac48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaab0`](#insn-00baaab0) 範囲 `[['00baaab0', '00baaad3']]`
  - `CONDITIONAL_JUMP` [`00baaad0`](#insn-00baaad0) → [`00baac30`](#insn-00baac30)
  - `FALL_THROUGH` [`00baaad0`](#insn-00baaad0) → [`00baaad4`](#insn-00baaad4)
- ブロック [`00baaad4`](#insn-00baaad4) 範囲 `[['00baaad4', '00baaaeb']]`
  - `UNCONDITIONAL_JUMP` [`00baaae8`](#insn-00baaae8) → [`00baab04`](#insn-00baab04)
- ブロック [`00baaaec`](#insn-00baaaec) 範囲 `[['00baaaec', '00baaaef']]`
  - `FALL_THROUGH` [`00baaaec`](#insn-00baaaec) → [`00baaaf0`](#insn-00baaaf0)
- ブロック [`00baaaf0`](#insn-00baaaf0) 範囲 `[['00baaaf0', '00baaaf3']]`
  - `FALL_THROUGH` [`00baaaf0`](#insn-00baaaf0) → [`00baaaf4`](#insn-00baaaf4)
- ブロック [`00baaaf4`](#insn-00baaaf4) 範囲 `[['00baaaf4', '00baab03']]`
  - `CONDITIONAL_JUMP` [`00baab00`](#insn-00baab00) → [`00baac2c`](#insn-00baac2c)
  - `FALL_THROUGH` [`00baab00`](#insn-00baab00) → [`00baab04`](#insn-00baab04)
- ブロック [`00baab04`](#insn-00baab04) 範囲 `[['00baab04', '00baab0f']]`
  - `CONDITIONAL_JUMP` [`00baab0c`](#insn-00baab0c) → [`00baaaec`](#insn-00baaaec)
  - `FALL_THROUGH` [`00baab0c`](#insn-00baab0c) → [`00baab10`](#insn-00baab10)
- ブロック [`00baab10`](#insn-00baab10) 範囲 `[['00baab10', '00baab23']]`
  - `CONDITIONAL_JUMP` [`00baab20`](#insn-00baab20) → [`00baab30`](#insn-00baab30)
  - `FALL_THROUGH` [`00baab20`](#insn-00baab20) → [`00baab24`](#insn-00baab24)
- ブロック [`00baab24`](#insn-00baab24) 範囲 `[['00baab24', '00baab2f']]`
  - `FALL_THROUGH` [`00baab2c`](#insn-00baab2c) → [`00baab30`](#insn-00baab30)
- ブロック [`00baab30`](#insn-00baab30) 範囲 `[['00baab30', '00baab3f']]`
  - `CONDITIONAL_JUMP` [`00baab3c`](#insn-00baab3c) → [`00baab4c`](#insn-00baab4c)
  - `FALL_THROUGH` [`00baab3c`](#insn-00baab3c) → [`00baab40`](#insn-00baab40)
- ブロック [`00baab40`](#insn-00baab40) 範囲 `[['00baab40', '00baab4b']]`
  - `FALL_THROUGH` [`00baab48`](#insn-00baab48) → [`00baab4c`](#insn-00baab4c)
- ブロック [`00baab4c`](#insn-00baab4c) 範囲 `[['00baab4c', '00baab5b']]`
  - `CONDITIONAL_JUMP` [`00baab58`](#insn-00baab58) → [`00baab68`](#insn-00baab68)
  - `FALL_THROUGH` [`00baab58`](#insn-00baab58) → [`00baab5c`](#insn-00baab5c)
- ブロック [`00baab5c`](#insn-00baab5c) 範囲 `[['00baab5c', '00baab67']]`
  - `FALL_THROUGH` [`00baab64`](#insn-00baab64) → [`00baab68`](#insn-00baab68)
- ブロック [`00baab68`](#insn-00baab68) 範囲 `[['00baab68', '00baab77']]`
  - `CONDITIONAL_JUMP` [`00baab74`](#insn-00baab74) → [`00baab84`](#insn-00baab84)
  - `FALL_THROUGH` [`00baab74`](#insn-00baab74) → [`00baab78`](#insn-00baab78)
- ブロック [`00baab78`](#insn-00baab78) 範囲 `[['00baab78', '00baab83']]`
  - `FALL_THROUGH` [`00baab80`](#insn-00baab80) → [`00baab84`](#insn-00baab84)
- ブロック [`00baab84`](#insn-00baab84) 範囲 `[['00baab84', '00baab93']]`
  - `CONDITIONAL_JUMP` [`00baab90`](#insn-00baab90) → [`00baaba0`](#insn-00baaba0)
  - `FALL_THROUGH` [`00baab90`](#insn-00baab90) → [`00baab94`](#insn-00baab94)
- ブロック [`00baab94`](#insn-00baab94) 範囲 `[['00baab94', '00baab9f']]`
  - `FALL_THROUGH` [`00baab9c`](#insn-00baab9c) → [`00baaba0`](#insn-00baaba0)
- ブロック [`00baaba0`](#insn-00baaba0) 範囲 `[['00baaba0', '00baabaf']]`
  - `CONDITIONAL_JUMP` [`00baabac`](#insn-00baabac) → [`00baabbc`](#insn-00baabbc)
  - `FALL_THROUGH` [`00baabac`](#insn-00baabac) → [`00baabb0`](#insn-00baabb0)
- ブロック [`00baabb0`](#insn-00baabb0) 範囲 `[['00baabb0', '00baabbb']]`
  - `FALL_THROUGH` [`00baabb8`](#insn-00baabb8) → [`00baabbc`](#insn-00baabbc)
- ブロック [`00baabbc`](#insn-00baabbc) 範囲 `[['00baabbc', '00baabcb']]`
  - `CONDITIONAL_JUMP` [`00baabc8`](#insn-00baabc8) → [`00baabd8`](#insn-00baabd8)
  - `FALL_THROUGH` [`00baabc8`](#insn-00baabc8) → [`00baabcc`](#insn-00baabcc)
- ブロック [`00baabcc`](#insn-00baabcc) 範囲 `[['00baabcc', '00baabd7']]`
  - `FALL_THROUGH` [`00baabd4`](#insn-00baabd4) → [`00baabd8`](#insn-00baabd8)
- ブロック [`00baabd8`](#insn-00baabd8) 範囲 `[['00baabd8', '00baabe7']]`
  - `CONDITIONAL_JUMP` [`00baabe4`](#insn-00baabe4) → [`00baabf4`](#insn-00baabf4)
  - `FALL_THROUGH` [`00baabe4`](#insn-00baabe4) → [`00baabe8`](#insn-00baabe8)
- ブロック [`00baabe8`](#insn-00baabe8) 範囲 `[['00baabe8', '00baabf3']]`
  - `FALL_THROUGH` [`00baabf0`](#insn-00baabf0) → [`00baabf4`](#insn-00baabf4)
- ブロック [`00baabf4`](#insn-00baabf4) 範囲 `[['00baabf4', '00baac03']]`
  - `CONDITIONAL_JUMP` [`00baac00`](#insn-00baac00) → [`00baac10`](#insn-00baac10)
  - `FALL_THROUGH` [`00baac00`](#insn-00baac00) → [`00baac04`](#insn-00baac04)
- ブロック [`00baac04`](#insn-00baac04) 範囲 `[['00baac04', '00baac0f']]`
  - `FALL_THROUGH` [`00baac0c`](#insn-00baac0c) → [`00baac10`](#insn-00baac10)
- ブロック [`00baac10`](#insn-00baac10) 範囲 `[['00baac10', '00baac1f']]`
  - `CONDITIONAL_JUMP` [`00baac1c`](#insn-00baac1c) → [`00baaaf4`](#insn-00baaaf4)
  - `FALL_THROUGH` [`00baac1c`](#insn-00baac1c) → [`00baac20`](#insn-00baac20)
- ブロック [`00baac20`](#insn-00baac20) 範囲 `[['00baac20', '00baac2b']]`
  - `UNCONDITIONAL_JUMP` [`00baac28`](#insn-00baac28) → [`00baaaf0`](#insn-00baaaf0)
- ブロック [`00baac2c`](#insn-00baac2c) 範囲 `[['00baac2c', '00baac2f']]`
  - `FALL_THROUGH` [`00baac2c`](#insn-00baac2c) → [`00baac30`](#insn-00baac30)
- ブロック [`00baac30`](#insn-00baac30) 範囲 `[['00baac30', '00baac4b']]`

## 命令位置別の参照

- [`00baaab4`](#insn-00baaab4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaab8`](#insn-00baaab8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaabc`](#insn-00baaabc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaac0`](#insn-00baaac0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaad0`](#insn-00baaad0) → [`00baac30`](#insn-00baac30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaae8`](#insn-00baaae8) → [`00baab04`](#insn-00baab04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaaec`](#insn-00baaaec) → `002fb120`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab00`](#insn-00baab00) → [`00baac2c`](#insn-00baac2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab0c`](#insn-00baab0c) → [`00baaaec`](#insn-00baaaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab1c`](#insn-00baab1c) → [`00be1950`](../00be1/00be1950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1950` · 推定シンボル `None` · 推定型 `None`
- [`00baab20`](#insn-00baab20) → [`00baab30`](#insn-00baab30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab38`](#insn-00baab38) → [`00be1960`](../00be1/00be1960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1960` · 推定シンボル `None` · 推定型 `None`
- [`00baab3c`](#insn-00baab3c) → [`00baab4c`](#insn-00baab4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab54`](#insn-00baab54) → [`00be1980`](../00be1/00be1980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1980` · 推定シンボル `None` · 推定型 `None`
- [`00baab58`](#insn-00baab58) → [`00baab68`](#insn-00baab68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab70`](#insn-00baab70) → [`00be1990`](../00be1/00be1990.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1990` · 推定シンボル `None` · 推定型 `None`
- [`00baab74`](#insn-00baab74) → [`00baab84`](#insn-00baab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baab8c`](#insn-00baab8c) → [`00be18b0`](../00be1/00be18b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be18b0` · 推定シンボル `None` · 推定型 `None`
- [`00baab90`](#insn-00baab90) → [`00baaba0`](#insn-00baaba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baaba8`](#insn-00baaba8) → [`00be19a0`](../00be1/00be19a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19a0` · 推定シンボル `None` · 推定型 `None`
- [`00baabac`](#insn-00baabac) → [`00baabbc`](#insn-00baabbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabc4`](#insn-00baabc4) → [`00be19b0`](../00be1/00be19b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19b0` · 推定シンボル `None` · 推定型 `None`
- [`00baabc8`](#insn-00baabc8) → [`00baabd8`](#insn-00baabd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabe0`](#insn-00baabe0) → [`00be19c0`](../00be1/00be19c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19c0` · 推定シンボル `None` · 推定型 `None`
- [`00baabe4`](#insn-00baabe4) → [`00baabf4`](#insn-00baabf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabfc`](#insn-00baabfc) → [`00be19d0`](../00be1/00be19d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19d0` · 推定シンボル `None` · 推定型 `None`
- [`00baac00`](#insn-00baac00) → [`00baac10`](#insn-00baac10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac18`](#insn-00baac18) → [`00be1970`](../00be1/00be1970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1970` · 推定シンボル `None` · 推定型 `None`
- [`00baac1c`](#insn-00baac1c) → [`00baaaf4`](#insn-00baaaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac28`](#insn-00baac28) → [`00baaaf0`](#insn-00baaaf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac34`](#insn-00baac34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac38`](#insn-00baac38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac3c`](#insn-00baac3c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac40`](#insn-00baac40) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaab4`](#insn-00baaab4)

~~~json
{
  "source": "00baaab4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaab8`](#insn-00baaab8)

~~~json
{
  "source": "00baaab8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaabc`](#insn-00baaabc)

~~~json
{
  "source": "00baaabc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaac0`](#insn-00baaac0)

~~~json
{
  "source": "00baaac0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaad0`](#insn-00baaad0)

~~~json
{
  "source": "00baaad0",
  "target": "00baac30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaae8`](#insn-00baaae8)

~~~json
{
  "source": "00baaae8",
  "target": "00baab04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaaec`](#insn-00baaaec)

~~~json
{
  "source": "00baaaec",
  "target": "002fb120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab00`](#insn-00baab00)

~~~json
{
  "source": "00baab00",
  "target": "00baac2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab0c`](#insn-00baab0c)

~~~json
{
  "source": "00baab0c",
  "target": "00baaaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab1c`](#insn-00baab1c)

~~~json
{
  "source": "00baab1c",
  "target": "00be1950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baab20`](#insn-00baab20)

~~~json
{
  "source": "00baab20",
  "target": "00baab30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab38`](#insn-00baab38)

~~~json
{
  "source": "00baab38",
  "target": "00be1960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baab3c`](#insn-00baab3c)

~~~json
{
  "source": "00baab3c",
  "target": "00baab4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab54`](#insn-00baab54)

~~~json
{
  "source": "00baab54",
  "target": "00be1980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baab58`](#insn-00baab58)

~~~json
{
  "source": "00baab58",
  "target": "00baab68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab70`](#insn-00baab70)

~~~json
{
  "source": "00baab70",
  "target": "00be1990",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baab74`](#insn-00baab74)

~~~json
{
  "source": "00baab74",
  "target": "00baab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baab8c`](#insn-00baab8c)

~~~json
{
  "source": "00baab8c",
  "target": "00be18b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baab90`](#insn-00baab90)

~~~json
{
  "source": "00baab90",
  "target": "00baaba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baaba8`](#insn-00baaba8)

~~~json
{
  "source": "00baaba8",
  "target": "00be19a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baabac`](#insn-00baabac)

~~~json
{
  "source": "00baabac",
  "target": "00baabbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabc4`](#insn-00baabc4)

~~~json
{
  "source": "00baabc4",
  "target": "00be19b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baabc8`](#insn-00baabc8)

~~~json
{
  "source": "00baabc8",
  "target": "00baabd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabe0`](#insn-00baabe0)

~~~json
{
  "source": "00baabe0",
  "target": "00be19c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baabe4`](#insn-00baabe4)

~~~json
{
  "source": "00baabe4",
  "target": "00baabf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabfc`](#insn-00baabfc)

~~~json
{
  "source": "00baabfc",
  "target": "00be19d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac00`](#insn-00baac00)

~~~json
{
  "source": "00baac00",
  "target": "00baac10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac18`](#insn-00baac18)

~~~json
{
  "source": "00baac18",
  "target": "00be1970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac1c`](#insn-00baac1c)

~~~json
{
  "source": "00baac1c",
  "target": "00baaaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac28`](#insn-00baac28)

~~~json
{
  "source": "00baac28",
  "target": "00baaaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac34`](#insn-00baac34)

~~~json
{
  "source": "00baac34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac38`](#insn-00baac38)

~~~json
{
  "source": "00baac38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac3c`](#insn-00baac3c)

~~~json
{
  "source": "00baac3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac40`](#insn-00baac40)

~~~json
{
  "source": "00baac40",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
