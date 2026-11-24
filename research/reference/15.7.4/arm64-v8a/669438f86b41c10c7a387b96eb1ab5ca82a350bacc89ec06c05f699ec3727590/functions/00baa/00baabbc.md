# 00baabbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baab78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baab78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0016.md#compare-ac3431ca1f4f1685a0ba7f9837c3cece)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c27604`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c27/00c27604.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0005.md#compare-4701055ccd23e6ea0c08f0e98780dda1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baabbc",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE5do_isEPKwS3_Pm",
  "size": 412,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1602342f78134560b6bd598c68adf2a44bf617a9703ea765a79fc884e81dbc7d",
  "source_text_sha256": "1602342f78134560b6bd598c68adf2a44bf617a9703ea765a79fc884e81dbc7d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baabbc",
        "00baad57"
      ]
    ],
    "bytes_sha256": "0506148988726f1201ebd78efa287db119b5e0d48560a527cf30f1bbf3097e4d",
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

- [00be19b0](../00be1/00be19b0.md)
- [00be1a50](../00be1/00be1a50.md)
- [00be1a60](../00be1/00be1a60.md)
- [00be1a70](../00be1/00be1a70.md)
- [00be1a80](../00be1/00be1a80.md)
- [00be1a90](../00be1/00be1a90.md)
- [00be1aa0](../00be1/00be1aa0.md)
- [00be1ab0](../00be1/00be1ab0.md)
- [00be1ac0](../00be1/00be1ac0.md)
- [00be1ad0](../00be1/00be1ad0.md)

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
LAB_00baabfc:
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
        goto LAB_00baabfc;
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
<a id="insn-00baabbc"></a> `00baabbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00baabc0"></a> `00baabc0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00baabc4"></a> `00baabc4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baabc8"></a> `00baabc8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baabcc"></a> `00baabcc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baabd0"></a> `00baabd0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00baabd4"></a> `00baabd4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00baabd8"></a> `00baabd8` | `3f 00 02 eb` | cmp x1,x2 | `FALL_THROUGH`
<a id="insn-00baabdc"></a> `00baabdc` | `00 0b 00 54` | b.eq 0x00baad3c | `CONDITIONAL_JUMP`
<a id="insn-00baabe0"></a> `00baabe0` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00baabe4"></a> `00baabe4` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00baabe8"></a> `00baabe8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00baabec"></a> `00baabec` | `98 ba ff b0` | adrp x24,0x2fb000 | `FALL_THROUGH`
<a id="insn-00baabf0"></a> `00baabf0` | `18 83 04 91` | add x24,x24,#0x120 | `FALL_THROUGH`
<a id="insn-00baabf4"></a> `00baabf4` | `07 00 00 14` | b 0x00baac10 | `UNCONDITIONAL_JUMP`
<a id="insn-00baabf8"></a> `00baabf8` | `08 7b 77 f8` | ldr x8,[x24, x23, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00baabfc"></a> `00baabfc` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac00"></a> `00baac00` | `73 12 00 91` | add x19,x19,#0x4 | `FALL_THROUGH`
<a id="insn-00baac04"></a> `00baac04` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00baac08"></a> `00baac08` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00baac0c"></a> `00baac0c` | `60 09 00 54` | b.eq 0x00baad38 | `CONDITIONAL_JUMP`
<a id="insn-00baac10"></a> `00baac10` | `77 02 40 b9` | ldr w23,[x19] | `FALL_THROUGH`
<a id="insn-00baac14"></a> `00baac14` | `ff fe 01 71` | cmp w23,#0x7f | `FALL_THROUGH`
<a id="insn-00baac18"></a> `00baac18` | `09 ff ff 54` | b.ls 0x00baabf8 | `CONDITIONAL_JUMP`
<a id="insn-00baac1c"></a> `00baac1c` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baac20"></a> `00baac20` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baac24"></a> `00baac24` | `bf 02 00 f9` | str xzr,[x21] | `FALL_THROUGH`
<a id="insn-00baac28"></a> `00baac28` | `8a db 00 94` | bl 0x00be1a50 | `UNCONDITIONAL_CALL`
<a id="insn-00baac2c"></a> `00baac2c` | `80 00 00 34` | cbz w0,0x00baac3c | `CONDITIONAL_JUMP`
<a id="insn-00baac30"></a> `00baac30` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac34"></a> `00baac34` | `08 01 40 b2` | orr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00baac38"></a> `00baac38` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac3c"></a> `00baac3c` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baac40"></a> `00baac40` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baac44"></a> `00baac44` | `87 db 00 94` | bl 0x00be1a60 | `UNCONDITIONAL_CALL`
<a id="insn-00baac48"></a> `00baac48` | `80 00 00 34` | cbz w0,0x00baac58 | `CONDITIONAL_JUMP`
<a id="insn-00baac4c"></a> `00baac4c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac50"></a> `00baac50` | `08 01 7f b2` | orr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00baac54"></a> `00baac54` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac58"></a> `00baac58` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baac5c"></a> `00baac5c` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baac60"></a> `00baac60` | `88 db 00 94` | bl 0x00be1a80 | `UNCONDITIONAL_CALL`
<a id="insn-00baac64"></a> `00baac64` | `80 00 00 34` | cbz w0,0x00baac74 | `CONDITIONAL_JUMP`
<a id="insn-00baac68"></a> `00baac68` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac6c"></a> `00baac6c` | `08 01 7e b2` | orr x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00baac70"></a> `00baac70` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac74"></a> `00baac74` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baac78"></a> `00baac78` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baac7c"></a> `00baac7c` | `85 db 00 94` | bl 0x00be1a90 | `UNCONDITIONAL_CALL`
<a id="insn-00baac80"></a> `00baac80` | `80 00 00 34` | cbz w0,0x00baac90 | `CONDITIONAL_JUMP`
<a id="insn-00baac84"></a> `00baac84` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac88"></a> `00baac88` | `08 01 7d b2` | orr x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00baac8c"></a> `00baac8c` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baac90"></a> `00baac90` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baac94"></a> `00baac94` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baac98"></a> `00baac98` | `46 db 00 94` | bl 0x00be19b0 | `UNCONDITIONAL_CALL`
<a id="insn-00baac9c"></a> `00baac9c` | `80 00 00 34` | cbz w0,0x00baacac | `CONDITIONAL_JUMP`
<a id="insn-00baaca0"></a> `00baaca0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baaca4"></a> `00baaca4` | `08 01 7c b2` | orr x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00baaca8"></a> `00baaca8` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baacac"></a> `00baacac` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baacb0"></a> `00baacb0` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baacb4"></a> `00baacb4` | `7b db 00 94` | bl 0x00be1aa0 | `UNCONDITIONAL_CALL`
<a id="insn-00baacb8"></a> `00baacb8` | `80 00 00 34` | cbz w0,0x00baacc8 | `CONDITIONAL_JUMP`
<a id="insn-00baacbc"></a> `00baacbc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baacc0"></a> `00baacc0` | `08 01 7b b2` | orr x8,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00baacc4"></a> `00baacc4` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baacc8"></a> `00baacc8` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baaccc"></a> `00baaccc` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baacd0"></a> `00baacd0` | `78 db 00 94` | bl 0x00be1ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00baacd4"></a> `00baacd4` | `80 00 00 34` | cbz w0,0x00baace4 | `CONDITIONAL_JUMP`
<a id="insn-00baacd8"></a> `00baacd8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baacdc"></a> `00baacdc` | `08 01 7a b2` | orr x8,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00baace0"></a> `00baace0` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baace4"></a> `00baace4` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baace8"></a> `00baace8` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baacec"></a> `00baacec` | `75 db 00 94` | bl 0x00be1ac0 | `UNCONDITIONAL_CALL`
<a id="insn-00baacf0"></a> `00baacf0` | `80 00 00 34` | cbz w0,0x00baad00 | `CONDITIONAL_JUMP`
<a id="insn-00baacf4"></a> `00baacf4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baacf8"></a> `00baacf8` | `08 01 79 b2` | orr x8,x8,#0x80 | `FALL_THROUGH`
<a id="insn-00baacfc"></a> `00baacfc` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baad00"></a> `00baad00` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baad04"></a> `00baad04` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baad08"></a> `00baad08` | `72 db 00 94` | bl 0x00be1ad0 | `UNCONDITIONAL_CALL`
<a id="insn-00baad0c"></a> `00baad0c` | `80 00 00 34` | cbz w0,0x00baad1c | `CONDITIONAL_JUMP`
<a id="insn-00baad10"></a> `00baad10` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baad14"></a> `00baad14` | `08 01 78 b2` | orr x8,x8,#0x100 | `FALL_THROUGH`
<a id="insn-00baad18"></a> `00baad18` | `a8 02 00 f9` | str x8,[x21] | `FALL_THROUGH`
<a id="insn-00baad1c"></a> `00baad1c` | `c1 0a 40 f9` | ldr x1,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00baad20"></a> `00baad20` | `e0 03 17 2a` | mov w0,w23 | `FALL_THROUGH`
<a id="insn-00baad24"></a> `00baad24` | `53 db 00 94` | bl 0x00be1a70 | `UNCONDITIONAL_CALL`
<a id="insn-00baad28"></a> `00baad28` | `c0 f6 ff 34` | cbz w0,0x00baac00 | `CONDITIONAL_JUMP`
<a id="insn-00baad2c"></a> `00baad2c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00baad30"></a> `00baad30` | `08 01 77 b2` | orr x8,x8,#0x200 | `FALL_THROUGH`
<a id="insn-00baad34"></a> `00baad34` | `b2 ff ff 17` | b 0x00baabfc | `UNCONDITIONAL_JUMP`
<a id="insn-00baad38"></a> `00baad38` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00baad3c"></a> `00baad3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00baad40"></a> `00baad40` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baad44"></a> `00baad44` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baad48"></a> `00baad48` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baad4c"></a> `00baad4c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00baad50"></a> `00baad50` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00baad54"></a> `00baad54` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baabbc`](#insn-00baabbc) 範囲 `[['00baabbc', '00baabdf']]`
  - `CONDITIONAL_JUMP` [`00baabdc`](#insn-00baabdc) → [`00baad3c`](#insn-00baad3c)
  - `FALL_THROUGH` [`00baabdc`](#insn-00baabdc) → [`00baabe0`](#insn-00baabe0)
- ブロック [`00baabe0`](#insn-00baabe0) 範囲 `[['00baabe0', '00baabf7']]`
  - `UNCONDITIONAL_JUMP` [`00baabf4`](#insn-00baabf4) → [`00baac10`](#insn-00baac10)
- ブロック [`00baabf8`](#insn-00baabf8) 範囲 `[['00baabf8', '00baabfb']]`
  - `FALL_THROUGH` [`00baabf8`](#insn-00baabf8) → [`00baabfc`](#insn-00baabfc)
- ブロック [`00baabfc`](#insn-00baabfc) 範囲 `[['00baabfc', '00baabff']]`
  - `FALL_THROUGH` [`00baabfc`](#insn-00baabfc) → [`00baac00`](#insn-00baac00)
- ブロック [`00baac00`](#insn-00baac00) 範囲 `[['00baac00', '00baac0f']]`
  - `CONDITIONAL_JUMP` [`00baac0c`](#insn-00baac0c) → [`00baad38`](#insn-00baad38)
  - `FALL_THROUGH` [`00baac0c`](#insn-00baac0c) → [`00baac10`](#insn-00baac10)
- ブロック [`00baac10`](#insn-00baac10) 範囲 `[['00baac10', '00baac1b']]`
  - `CONDITIONAL_JUMP` [`00baac18`](#insn-00baac18) → [`00baabf8`](#insn-00baabf8)
  - `FALL_THROUGH` [`00baac18`](#insn-00baac18) → [`00baac1c`](#insn-00baac1c)
- ブロック [`00baac1c`](#insn-00baac1c) 範囲 `[['00baac1c', '00baac2f']]`
  - `CONDITIONAL_JUMP` [`00baac2c`](#insn-00baac2c) → [`00baac3c`](#insn-00baac3c)
  - `FALL_THROUGH` [`00baac2c`](#insn-00baac2c) → [`00baac30`](#insn-00baac30)
- ブロック [`00baac30`](#insn-00baac30) 範囲 `[['00baac30', '00baac3b']]`
  - `FALL_THROUGH` [`00baac38`](#insn-00baac38) → [`00baac3c`](#insn-00baac3c)
- ブロック [`00baac3c`](#insn-00baac3c) 範囲 `[['00baac3c', '00baac4b']]`
  - `CONDITIONAL_JUMP` [`00baac48`](#insn-00baac48) → [`00baac58`](#insn-00baac58)
  - `FALL_THROUGH` [`00baac48`](#insn-00baac48) → [`00baac4c`](#insn-00baac4c)
- ブロック [`00baac4c`](#insn-00baac4c) 範囲 `[['00baac4c', '00baac57']]`
  - `FALL_THROUGH` [`00baac54`](#insn-00baac54) → [`00baac58`](#insn-00baac58)
- ブロック [`00baac58`](#insn-00baac58) 範囲 `[['00baac58', '00baac67']]`
  - `CONDITIONAL_JUMP` [`00baac64`](#insn-00baac64) → [`00baac74`](#insn-00baac74)
  - `FALL_THROUGH` [`00baac64`](#insn-00baac64) → [`00baac68`](#insn-00baac68)
- ブロック [`00baac68`](#insn-00baac68) 範囲 `[['00baac68', '00baac73']]`
  - `FALL_THROUGH` [`00baac70`](#insn-00baac70) → [`00baac74`](#insn-00baac74)
- ブロック [`00baac74`](#insn-00baac74) 範囲 `[['00baac74', '00baac83']]`
  - `CONDITIONAL_JUMP` [`00baac80`](#insn-00baac80) → [`00baac90`](#insn-00baac90)
  - `FALL_THROUGH` [`00baac80`](#insn-00baac80) → [`00baac84`](#insn-00baac84)
- ブロック [`00baac84`](#insn-00baac84) 範囲 `[['00baac84', '00baac8f']]`
  - `FALL_THROUGH` [`00baac8c`](#insn-00baac8c) → [`00baac90`](#insn-00baac90)
- ブロック [`00baac90`](#insn-00baac90) 範囲 `[['00baac90', '00baac9f']]`
  - `CONDITIONAL_JUMP` [`00baac9c`](#insn-00baac9c) → [`00baacac`](#insn-00baacac)
  - `FALL_THROUGH` [`00baac9c`](#insn-00baac9c) → [`00baaca0`](#insn-00baaca0)
- ブロック [`00baaca0`](#insn-00baaca0) 範囲 `[['00baaca0', '00baacab']]`
  - `FALL_THROUGH` [`00baaca8`](#insn-00baaca8) → [`00baacac`](#insn-00baacac)
- ブロック [`00baacac`](#insn-00baacac) 範囲 `[['00baacac', '00baacbb']]`
  - `CONDITIONAL_JUMP` [`00baacb8`](#insn-00baacb8) → [`00baacc8`](#insn-00baacc8)
  - `FALL_THROUGH` [`00baacb8`](#insn-00baacb8) → [`00baacbc`](#insn-00baacbc)
- ブロック [`00baacbc`](#insn-00baacbc) 範囲 `[['00baacbc', '00baacc7']]`
  - `FALL_THROUGH` [`00baacc4`](#insn-00baacc4) → [`00baacc8`](#insn-00baacc8)
- ブロック [`00baacc8`](#insn-00baacc8) 範囲 `[['00baacc8', '00baacd7']]`
  - `CONDITIONAL_JUMP` [`00baacd4`](#insn-00baacd4) → [`00baace4`](#insn-00baace4)
  - `FALL_THROUGH` [`00baacd4`](#insn-00baacd4) → [`00baacd8`](#insn-00baacd8)
- ブロック [`00baacd8`](#insn-00baacd8) 範囲 `[['00baacd8', '00baace3']]`
  - `FALL_THROUGH` [`00baace0`](#insn-00baace0) → [`00baace4`](#insn-00baace4)
- ブロック [`00baace4`](#insn-00baace4) 範囲 `[['00baace4', '00baacf3']]`
  - `CONDITIONAL_JUMP` [`00baacf0`](#insn-00baacf0) → [`00baad00`](#insn-00baad00)
  - `FALL_THROUGH` [`00baacf0`](#insn-00baacf0) → [`00baacf4`](#insn-00baacf4)
- ブロック [`00baacf4`](#insn-00baacf4) 範囲 `[['00baacf4', '00baacff']]`
  - `FALL_THROUGH` [`00baacfc`](#insn-00baacfc) → [`00baad00`](#insn-00baad00)
- ブロック [`00baad00`](#insn-00baad00) 範囲 `[['00baad00', '00baad0f']]`
  - `CONDITIONAL_JUMP` [`00baad0c`](#insn-00baad0c) → [`00baad1c`](#insn-00baad1c)
  - `FALL_THROUGH` [`00baad0c`](#insn-00baad0c) → [`00baad10`](#insn-00baad10)
- ブロック [`00baad10`](#insn-00baad10) 範囲 `[['00baad10', '00baad1b']]`
  - `FALL_THROUGH` [`00baad18`](#insn-00baad18) → [`00baad1c`](#insn-00baad1c)
- ブロック [`00baad1c`](#insn-00baad1c) 範囲 `[['00baad1c', '00baad2b']]`
  - `CONDITIONAL_JUMP` [`00baad28`](#insn-00baad28) → [`00baac00`](#insn-00baac00)
  - `FALL_THROUGH` [`00baad28`](#insn-00baad28) → [`00baad2c`](#insn-00baad2c)
- ブロック [`00baad2c`](#insn-00baad2c) 範囲 `[['00baad2c', '00baad37']]`
  - `UNCONDITIONAL_JUMP` [`00baad34`](#insn-00baad34) → [`00baabfc`](#insn-00baabfc)
- ブロック [`00baad38`](#insn-00baad38) 範囲 `[['00baad38', '00baad3b']]`
  - `FALL_THROUGH` [`00baad38`](#insn-00baad38) → [`00baad3c`](#insn-00baad3c)
- ブロック [`00baad3c`](#insn-00baad3c) 範囲 `[['00baad3c', '00baad57']]`

## 命令位置別の参照

- [`00baabc0`](#insn-00baabc0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabc4`](#insn-00baabc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabc8`](#insn-00baabc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabcc`](#insn-00baabcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabdc`](#insn-00baabdc) → [`00baad3c`](#insn-00baad3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabf4`](#insn-00baabf4) → [`00baac10`](#insn-00baac10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baabf8`](#insn-00baabf8) → `002fb120`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac0c`](#insn-00baac0c) → [`00baad38`](#insn-00baad38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac18`](#insn-00baac18) → [`00baabf8`](#insn-00baabf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac28`](#insn-00baac28) → [`00be1a50`](../00be1/00be1a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a50` · 推定シンボル `None` · 推定型 `None`
- [`00baac2c`](#insn-00baac2c) → [`00baac3c`](#insn-00baac3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac44`](#insn-00baac44) → [`00be1a60`](../00be1/00be1a60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a60` · 推定シンボル `None` · 推定型 `None`
- [`00baac48`](#insn-00baac48) → [`00baac58`](#insn-00baac58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac60`](#insn-00baac60) → [`00be1a80`](../00be1/00be1a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a80` · 推定シンボル `None` · 推定型 `None`
- [`00baac64`](#insn-00baac64) → [`00baac74`](#insn-00baac74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac7c`](#insn-00baac7c) → [`00be1a90`](../00be1/00be1a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a90` · 推定シンボル `None` · 推定型 `None`
- [`00baac80`](#insn-00baac80) → [`00baac90`](#insn-00baac90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baac98`](#insn-00baac98) → [`00be19b0`](../00be1/00be19b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19b0` · 推定シンボル `None` · 推定型 `None`
- [`00baac9c`](#insn-00baac9c) → [`00baacac`](#insn-00baacac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacb4`](#insn-00baacb4) → [`00be1aa0`](../00be1/00be1aa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1aa0` · 推定シンボル `None` · 推定型 `None`
- [`00baacb8`](#insn-00baacb8) → [`00baacc8`](#insn-00baacc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacd0`](#insn-00baacd0) → [`00be1ab0`](../00be1/00be1ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ab0` · 推定シンボル `None` · 推定型 `None`
- [`00baacd4`](#insn-00baacd4) → [`00baace4`](#insn-00baace4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baacec`](#insn-00baacec) → [`00be1ac0`](../00be1/00be1ac0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ac0` · 推定シンボル `None` · 推定型 `None`
- [`00baacf0`](#insn-00baacf0) → [`00baad00`](#insn-00baad00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad08`](#insn-00baad08) → [`00be1ad0`](../00be1/00be1ad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1ad0` · 推定シンボル `None` · 推定型 `None`
- [`00baad0c`](#insn-00baad0c) → [`00baad1c`](#insn-00baad1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad24`](#insn-00baad24) → [`00be1a70`](../00be1/00be1a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1a70` · 推定シンボル `None` · 推定型 `None`
- [`00baad28`](#insn-00baad28) → [`00baac00`](#insn-00baac00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad34`](#insn-00baad34) → [`00baabfc`](#insn-00baabfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad40`](#insn-00baad40) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad44`](#insn-00baad44) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad48`](#insn-00baad48) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baad4c`](#insn-00baad4c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baabc0`](#insn-00baabc0)

~~~json
{
  "source": "00baabc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabc4`](#insn-00baabc4)

~~~json
{
  "source": "00baabc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabc8`](#insn-00baabc8)

~~~json
{
  "source": "00baabc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabcc`](#insn-00baabcc)

~~~json
{
  "source": "00baabcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabdc`](#insn-00baabdc)

~~~json
{
  "source": "00baabdc",
  "target": "00baad3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabf4`](#insn-00baabf4)

~~~json
{
  "source": "00baabf4",
  "target": "00baac10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baabf8`](#insn-00baabf8)

~~~json
{
  "source": "00baabf8",
  "target": "002fb120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac0c`](#insn-00baac0c)

~~~json
{
  "source": "00baac0c",
  "target": "00baad38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac18`](#insn-00baac18)

~~~json
{
  "source": "00baac18",
  "target": "00baabf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac28`](#insn-00baac28)

~~~json
{
  "source": "00baac28",
  "target": "00be1a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac2c`](#insn-00baac2c)

~~~json
{
  "source": "00baac2c",
  "target": "00baac3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac44`](#insn-00baac44)

~~~json
{
  "source": "00baac44",
  "target": "00be1a60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac48`](#insn-00baac48)

~~~json
{
  "source": "00baac48",
  "target": "00baac58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac60`](#insn-00baac60)

~~~json
{
  "source": "00baac60",
  "target": "00be1a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac64`](#insn-00baac64)

~~~json
{
  "source": "00baac64",
  "target": "00baac74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac7c`](#insn-00baac7c)

~~~json
{
  "source": "00baac7c",
  "target": "00be1a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac80`](#insn-00baac80)

~~~json
{
  "source": "00baac80",
  "target": "00baac90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baac98`](#insn-00baac98)

~~~json
{
  "source": "00baac98",
  "target": "00be19b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baac9c`](#insn-00baac9c)

~~~json
{
  "source": "00baac9c",
  "target": "00baacac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacb4`](#insn-00baacb4)

~~~json
{
  "source": "00baacb4",
  "target": "00be1aa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baacb8`](#insn-00baacb8)

~~~json
{
  "source": "00baacb8",
  "target": "00baacc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacd0`](#insn-00baacd0)

~~~json
{
  "source": "00baacd0",
  "target": "00be1ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baacd4`](#insn-00baacd4)

~~~json
{
  "source": "00baacd4",
  "target": "00baace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baacec`](#insn-00baacec)

~~~json
{
  "source": "00baacec",
  "target": "00be1ac0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baacf0`](#insn-00baacf0)

~~~json
{
  "source": "00baacf0",
  "target": "00baad00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad08`](#insn-00baad08)

~~~json
{
  "source": "00baad08",
  "target": "00be1ad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad0c`](#insn-00baad0c)

~~~json
{
  "source": "00baad0c",
  "target": "00baad1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad24`](#insn-00baad24)

~~~json
{
  "source": "00baad24",
  "target": "00be1a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00baad28`](#insn-00baad28)

~~~json
{
  "source": "00baad28",
  "target": "00baac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad34`](#insn-00baad34)

~~~json
{
  "source": "00baad34",
  "target": "00baabfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad40`](#insn-00baad40)

~~~json
{
  "source": "00baad40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad44`](#insn-00baad44)

~~~json
{
  "source": "00baad44",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad48`](#insn-00baad48)

~~~json
{
  "source": "00baad48",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baad4c`](#insn-00baad4c)

~~~json
{
  "source": "00baad4c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
