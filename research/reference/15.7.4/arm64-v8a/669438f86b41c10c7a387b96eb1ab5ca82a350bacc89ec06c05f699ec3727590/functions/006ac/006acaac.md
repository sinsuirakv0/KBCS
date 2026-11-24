# 006acaac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `006acaac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ac/006acaac.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0020.md#compare-450c93f3f6bddc69e9c217870cb1fcd0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0042.md#review-68b5dacf6d1d339c7de24397156bd85a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006acaac",
  "name": "FUN_006acaac",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "766d9ae780ef7aa0ff5e5669847aa4a04c5ec274a9762e17e144e766092c0016",
  "source_text_sha256": "766d9ae780ef7aa0ff5e5669847aa4a04c5ec274a9762e17e144e766092c0016",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006acaac",
        "006acd0b"
      ]
    ],
    "bytes_sha256": "f4eb1bdb062a6055a11debf5f8c03ddc31553b21d7452cbeab706be89fd5d32c",
    "instruction_count": 152,
    "instruction_bytes": 608,
    "body_bytes": 608,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a823d8](../00a82/00a823d8.md)

## 呼び出し先

- [0063eb28](../0063e/0063eb28.md)
- [0081f580](../0081f/0081f580.md)
- [00bdb600](../00bdb/00bdb600.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4109 bytes

~~~c

undefined8 FUN_006acaac(int *param_1)

{
  wchar_t *pwVar1;
  wchar_t *pwVar2;
  wchar_t wVar3;
  bool bVar4;
  bool bVar5;
  wchar_t wVar6;
  int iVar7;
  wchar_t wVar8;
  long lVar9;
  wchar_t *pwVar10;
  wchar_t *pwVar11;
  
  lVar9 = FUN_0081f580();
  wVar3 = *(wchar_t *)(lVar9 + (long)*param_1 * 4 + 0x49734);
  lVar9 = FUN_0081f580();
  if (*(int *)(BYTE_ARRAY_0032fef1 + lVar9 + 0x1b) == 3) {
    pwVar11 = *(wchar_t **)(param_1 + 8);
    if (pwVar11 != *(wchar_t **)(param_1 + 10)) {
      pwVar1 = *(wchar_t **)(param_1 + 0xe);
      pwVar2 = *(wchar_t **)(param_1 + 0x10);
      do {
        if (pwVar1 == pwVar2) {
          return 0;
        }
        wVar8 = *pwVar1;
        wVar6 = FUN_0063eb28(*param_1);
        if (wVar8 <= wVar6) {
          pwVar11 = *(wchar_t **)(param_1 + 10);
          pwVar10 = wmemchr(*(wchar_t **)(param_1 + 8),wVar8,
                            (long)pwVar11 - (long)*(wchar_t **)(param_1 + 8) >> 2);
          if (pwVar10 != (wchar_t *)0x0) {
            pwVar11 = pwVar10;
          }
          if (pwVar11 == *(wchar_t **)(param_1 + 10)) break;
        }
        pwVar1 = pwVar1 + 1;
      } while( true );
    }
  }
  else {
    pwVar11 = *(wchar_t **)(param_1 + 10);
  }
  if (*(wchar_t **)(param_1 + 8) == pwVar11) {
    bVar4 = true;
  }
  else {
    pwVar1 = *(wchar_t **)(param_1 + 0x10);
    bVar4 = true;
    for (pwVar11 = *(wchar_t **)(param_1 + 0xe); pwVar11 != pwVar1; pwVar11 = pwVar11 + 1) {
      wVar8 = *pwVar11;
      wVar6 = FUN_0063eb28(*param_1);
      if (wVar8 <= wVar6) {
        pwVar2 = *(wchar_t **)(param_1 + 10);
        pwVar10 = wmemchr(*(wchar_t **)(param_1 + 8),wVar8,
                          (long)pwVar2 - (long)*(wchar_t **)(param_1 + 8) >> 2);
        if (pwVar10 != (wchar_t *)0x0) {
          pwVar2 = pwVar10;
        }
        bVar4 = (bool)(pwVar2 != *(wchar_t **)(param_1 + 10) & bVar4);
      }
    }
  }
  pwVar11 = *(wchar_t **)(param_1 + 0xe);
  pwVar1 = *(wchar_t **)(param_1 + 0x10);
  if (pwVar11 != pwVar1) {
    bVar5 = false;
    do {
                    /* catch() { ... } // from try @ 006acc94 with catch @ 006acbf4 */
      wVar8 = *pwVar11;
      wVar6 = FUN_0063eb28(*param_1);
      if (wVar8 <= wVar6) {
        if (wVar3 == wVar8) {
          if (bVar4) {
            return 0;
          }
          pwVar10 = *(wchar_t **)(param_1 + 8);
          pwVar2 = *(wchar_t **)(param_1 + 10);
          if (pwVar10 == pwVar2) {
            return 0;
          }
          pwVar10 = wmemchr(pwVar10,wVar3,(long)pwVar2 - (long)pwVar10 >> 2);
          if (pwVar10 != (wchar_t *)0x0) {
            pwVar2 = pwVar10;
          }
          if (pwVar2 == *(wchar_t **)(param_1 + 10)) {
            return 0;
          }
        }
        bVar5 = true;
      }
      pwVar11 = pwVar11 + 1;
    } while (pwVar11 != pwVar1);
    if (bVar5) {
      return 1;
    }
  }
  lVar9 = FUN_0081f580();
  if (*(int *)(BYTE_ARRAY_0032fef1 + lVar9 + 0x1b) == 7) {
    iVar7 = FUN_0063eb28(*param_1);
    if (iVar7 < 2) {
      return 0;
    }
    if (L'\x01' < wVar3) {
      return 0;
    }
                    /* try { // try from 006acc88 to 007acc93 has its CatchHandler @ 006acd1c */
    if (*(long *)(param_1 + 8) != *(long *)(param_1 + 10)) {
                    /* try { // try from 006acc94 to 007acdaf has its CatchHandler @ 006acbf4 */
      pwVar11 = *(wchar_t **)(param_1 + 0xe);
      pwVar1 = *(wchar_t **)(param_1 + 0x10);
      if (pwVar11 == pwVar1) {
        return 1;
      }
      do {
        wVar3 = *pwVar11;
        wVar8 = FUN_0063eb28(*param_1);
        if (wVar3 <= wVar8) {
          pwVar2 = *(wchar_t **)(param_1 + 10);
          pwVar10 = wmemchr(*(wchar_t **)(param_1 + 8),wVar3,
                            (long)pwVar2 - (long)*(wchar_t **)(param_1 + 8) >> 2);
          if (pwVar10 != (wchar_t *)0x0) {
            pwVar2 = pwVar10;
          }
          if (pwVar2 == *(wchar_t **)(param_1 + 10)) {
            return 0;
          }
        }
        pwVar11 = pwVar11 + 1;
        if (pwVar11 == pwVar1) {
          return 1;
        }
      } while( true );
    }
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006acaac"></a> `006acaac` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-006acab0"></a> `006acab0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006acab4"></a> `006acab4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006acab8"></a> `006acab8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006acabc"></a> `006acabc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006acac0"></a> `006acac0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006acac4"></a> `006acac4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006acac8"></a> `006acac8` | `ae ca 05 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006acacc"></a> `006acacc` | `68 02 80 b9` | ldrsw x8,[x19] | `FALL_THROUGH`
<a id="insn-006acad0"></a> `006acad0` | `89 e6 92 52` | mov w9,#0x9734 | `FALL_THROUGH`
<a id="insn-006acad4"></a> `006acad4` | `89 00 a0 72` | movk w9,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-006acad8"></a> `006acad8` | `08 08 08 8b` | add x8,x0,x8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-006acadc"></a> `006acadc` | `14 69 69 b8` | ldr w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006acae0"></a> `006acae0` | `a8 ca 05 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006acae4"></a> `006acae4` | `88 e1 9f 52` | mov w8,#0xff0c | `FALL_THROUGH`
<a id="insn-006acae8"></a> `006acae8` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-006acaec"></a> `006acaec` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006acaf0"></a> `006acaf0` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-006acaf4"></a> `006acaf4` | `61 03 00 54` | b.ne 0x006acb60 | `CONDITIONAL_JUMP`
<a id="insn-006acaf8"></a> `006acaf8` | `68 26 42 a9` | ldp x8,x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006acafc"></a> `006acafc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006acb00"></a> `006acb00` | `20 03 00 54` | b.eq 0x006acb64 | `CONDITIONAL_JUMP`
<a id="insn-006acb04"></a> `006acb04` | `76 de 43 a9` | ldp x22,x23,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-006acb08"></a> `006acb08` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-006acb0c"></a> `006acb0c` | `a1 00 00 54` | b.ne 0x006acb20 | `CONDITIONAL_JUMP`
<a id="insn-006acb10"></a> `006acb10` | `78 00 00 14` | b 0x006accf0 | `UNCONDITIONAL_JUMP`
<a id="insn-006acb14"></a> `006acb14` | `d6 12 00 91` | add x22,x22,#0x4 | `FALL_THROUGH`
<a id="insn-006acb18"></a> `006acb18` | `df 02 17 eb` | cmp x22,x23 | `FALL_THROUGH`
<a id="insn-006acb1c"></a> `006acb1c` | `a0 0e 00 54` | b.eq 0x006accf0 | `CONDITIONAL_JUMP`
<a id="insn-006acb20"></a> `006acb20` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-006acb24"></a> `006acb24` | `d5 02 40 b9` | ldr w21,[x22] | `FALL_THROUGH`
<a id="insn-006acb28"></a> `006acb28` | `00 48 fe 97` | bl 0x0063eb28 | `UNCONDITIONAL_CALL`
<a id="insn-006acb2c"></a> `006acb2c` | `bf 02 00 6b` | cmp w21,w0 | `FALL_THROUGH`
<a id="insn-006acb30"></a> `006acb30` | `2c ff ff 54` | b.gt 0x006acb14 | `CONDITIONAL_JUMP`
<a id="insn-006acb34"></a> `006acb34` | `60 62 42 a9` | ldp x0,x24,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006acb38"></a> `006acb38` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-006acb3c"></a> `006acb3c` | `08 03 00 cb` | sub x8,x24,x0 | `FALL_THROUGH`
<a id="insn-006acb40"></a> `006acb40` | `02 fd 42 93` | asr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006acb44"></a> `006acb44` | `af ba 14 94` | bl 0x00bdb600 | `UNCONDITIONAL_CALL`
<a id="insn-006acb48"></a> `006acb48` | `69 16 40 f9` | ldr x9,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-006acb4c"></a> `006acb4c` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-006acb50"></a> `006acb50` | `08 03 80 9a` | csel x8,x24,x0,eq | `FALL_THROUGH`
<a id="insn-006acb54"></a> `006acb54` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006acb58"></a> `006acb58` | `e1 fd ff 54` | b.ne 0x006acb14 | `CONDITIONAL_JUMP`
<a id="insn-006acb5c"></a> `006acb5c` | `02 00 00 14` | b 0x006acb64 | `UNCONDITIONAL_JUMP`
<a id="insn-006acb60"></a> `006acb60` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-006acb64"></a> `006acb64` | `69 12 40 f9` | ldr x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006acb68"></a> `006acb68` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-006acb6c"></a> `006acb6c` | `00 03 00 54` | b.eq 0x006acbcc | `CONDITIONAL_JUMP`
<a id="insn-006acb70"></a> `006acb70` | `77 e2 43 a9` | ldp x23,x24,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-006acb74"></a> `006acb74` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-006acb78"></a> `006acb78` | `02 00 00 14` | b 0x006acb80 | `UNCONDITIONAL_JUMP`
<a id="insn-006acb7c"></a> `006acb7c` | `f7 12 00 91` | add x23,x23,#0x4 | `FALL_THROUGH`
<a id="insn-006acb80"></a> `006acb80` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-006acb84"></a> `006acb84` | `60 02 00 54` | b.eq 0x006acbd0 | `CONDITIONAL_JUMP`
<a id="insn-006acb88"></a> `006acb88` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-006acb8c"></a> `006acb8c` | `f5 02 40 b9` | ldr w21,[x23] | `FALL_THROUGH`
<a id="insn-006acb90"></a> `006acb90` | `e6 47 fe 97` | bl 0x0063eb28 | `UNCONDITIONAL_CALL`
<a id="insn-006acb94"></a> `006acb94` | `bf 02 00 6b` | cmp w21,w0 | `FALL_THROUGH`
<a id="insn-006acb98"></a> `006acb98` | `2c ff ff 54` | b.gt 0x006acb7c | `CONDITIONAL_JUMP`
<a id="insn-006acb9c"></a> `006acb9c` | `60 66 42 a9` | ldp x0,x25,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006acba0"></a> `006acba0` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-006acba4"></a> `006acba4` | `28 03 00 cb` | sub x8,x25,x0 | `FALL_THROUGH`
<a id="insn-006acba8"></a> `006acba8` | `02 fd 42 93` | asr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006acbac"></a> `006acbac` | `95 ba 14 94` | bl 0x00bdb600 | `UNCONDITIONAL_CALL`
<a id="insn-006acbb0"></a> `006acbb0` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-006acbb4"></a> `006acbb4` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-006acbb8"></a> `006acbb8` | `29 03 80 9a` | csel x9,x25,x0,eq | `FALL_THROUGH`
<a id="insn-006acbbc"></a> `006acbbc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-006acbc0"></a> `006acbc0` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-006acbc4"></a> `006acbc4` | `16 01 16 0a` | and w22,w8,w22 | `FALL_THROUGH`
<a id="insn-006acbc8"></a> `006acbc8` | `ed ff ff 17` | b 0x006acb7c | `UNCONDITIONAL_JUMP`
<a id="insn-006acbcc"></a> `006acbcc` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-006acbd0"></a> `006acbd0` | `75 de 43 a9` | ldp x21,x23,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-006acbd4"></a> `006acbd4` | `bf 02 17 eb` | cmp x21,x23 | `FALL_THROUGH`
<a id="insn-006acbd8"></a> `006acbd8` | `e0 03 00 54` | b.eq 0x006acc54 | `CONDITIONAL_JUMP`
<a id="insn-006acbdc"></a> `006acbdc` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-006acbe0"></a> `006acbe0` | `05 00 00 14` | b 0x006acbf4 | `UNCONDITIONAL_JUMP`
<a id="insn-006acbe4"></a> `006acbe4` | `38 00 80 52` | mov w24,#0x1 | `FALL_THROUGH`
<a id="insn-006acbe8"></a> `006acbe8` | `b5 12 00 91` | add x21,x21,#0x4 | `FALL_THROUGH`
<a id="insn-006acbec"></a> `006acbec` | `bf 02 17 eb` | cmp x21,x23 | `FALL_THROUGH`
<a id="insn-006acbf0"></a> `006acbf0` | `c0 02 00 54` | b.eq 0x006acc48 | `CONDITIONAL_JUMP`
<a id="insn-006acbf4"></a> `006acbf4` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-006acbf8"></a> `006acbf8` | `b9 02 40 b9` | ldr w25,[x21] | `FALL_THROUGH`
<a id="insn-006acbfc"></a> `006acbfc` | `cb 47 fe 97` | bl 0x0063eb28 | `UNCONDITIONAL_CALL`
<a id="insn-006acc00"></a> `006acc00` | `3f 03 00 6b` | cmp w25,w0 | `FALL_THROUGH`
<a id="insn-006acc04"></a> `006acc04` | `2c ff ff 54` | b.gt 0x006acbe8 | `CONDITIONAL_JUMP`
<a id="insn-006acc08"></a> `006acc08` | `9f 02 19 6b` | cmp w20,w25 | `FALL_THROUGH`
<a id="insn-006acc0c"></a> `006acc0c` | `c1 fe ff 54` | b.ne 0x006acbe4 | `CONDITIONAL_JUMP`
<a id="insn-006acc10"></a> `006acc10` | `16 07 00 37` | tbnz w22,#0x0,0x006accf0 | `CONDITIONAL_JUMP`
<a id="insn-006acc14"></a> `006acc14` | `60 62 42 a9` | ldp x0,x24,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006acc18"></a> `006acc18` | `1f 00 18 eb` | cmp x0,x24 | `FALL_THROUGH`
<a id="insn-006acc1c"></a> `006acc1c` | `a0 06 00 54` | b.eq 0x006accf0 | `CONDITIONAL_JUMP`
<a id="insn-006acc20"></a> `006acc20` | `08 03 00 cb` | sub x8,x24,x0 | `FALL_THROUGH`
<a id="insn-006acc24"></a> `006acc24` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-006acc28"></a> `006acc28` | `02 fd 42 93` | asr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006acc2c"></a> `006acc2c` | `75 ba 14 94` | bl 0x00bdb600 | `UNCONDITIONAL_CALL`
<a id="insn-006acc30"></a> `006acc30` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-006acc34"></a> `006acc34` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-006acc38"></a> `006acc38` | `09 03 80 9a` | csel x9,x24,x0,eq | `FALL_THROUGH`
<a id="insn-006acc3c"></a> `006acc3c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-006acc40"></a> `006acc40` | `21 fd ff 54` | b.ne 0x006acbe4 | `CONDITIONAL_JUMP`
<a id="insn-006acc44"></a> `006acc44` | `2b 00 00 14` | b 0x006accf0 | `UNCONDITIONAL_JUMP`
<a id="insn-006acc48"></a> `006acc48` | `78 00 00 36` | tbz w24,#0x0,0x006acc54 | `CONDITIONAL_JUMP`
<a id="insn-006acc4c"></a> `006acc4c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-006acc50"></a> `006acc50` | `29 00 00 14` | b 0x006accf4 | `UNCONDITIONAL_JUMP`
<a id="insn-006acc54"></a> `006acc54` | `4b ca 05 94` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-006acc58"></a> `006acc58` | `88 e1 9f 52` | mov w8,#0xff0c | `FALL_THROUGH`
<a id="insn-006acc5c"></a> `006acc5c` | `48 06 a0 72` | movk w8,#0x32, LSL #16 | `FALL_THROUGH`
<a id="insn-006acc60"></a> `006acc60` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006acc64"></a> `006acc64` | `1f 1d 00 71` | cmp w8,#0x7 | `FALL_THROUGH`
<a id="insn-006acc68"></a> `006acc68` | `41 04 00 54` | b.ne 0x006accf0 | `CONDITIONAL_JUMP`
<a id="insn-006acc6c"></a> `006acc6c` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-006acc70"></a> `006acc70` | `ae 47 fe 97` | bl 0x0063eb28 | `UNCONDITIONAL_CALL`
<a id="insn-006acc74"></a> `006acc74` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-006acc78"></a> `006acc78` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-006acc7c"></a> `006acc7c` | `cb 03 00 54` | b.lt 0x006accf4 | `CONDITIONAL_JUMP`
<a id="insn-006acc80"></a> `006acc80` | `9f 06 00 71` | cmp w20,#0x1 | `FALL_THROUGH`
<a id="insn-006acc84"></a> `006acc84` | `8c 03 00 54` | b.gt 0x006accf4 | `CONDITIONAL_JUMP`
<a id="insn-006acc88"></a> `006acc88` | `68 26 42 a9` | ldp x8,x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006acc8c"></a> `006acc8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006acc90"></a> `006acc90` | `00 03 00 54` | b.eq 0x006accf0 | `CONDITIONAL_JUMP`
<a id="insn-006acc94"></a> `006acc94` | `75 da 43 a9` | ldp x21,x22,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-006acc98"></a> `006acc98` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-006acc9c"></a> `006acc9c` | `c1 00 00 54` | b.ne 0x006accb4 | `CONDITIONAL_JUMP`
<a id="insn-006acca0"></a> `006acca0` | `eb ff ff 17` | b 0x006acc4c | `UNCONDITIONAL_JUMP`
<a id="insn-006acca4"></a> `006acca4` | `b5 12 00 91` | add x21,x21,#0x4 | `FALL_THROUGH`
<a id="insn-006acca8"></a> `006acca8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-006accac"></a> `006accac` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-006accb0"></a> `006accb0` | `20 02 00 54` | b.eq 0x006accf4 | `CONDITIONAL_JUMP`
<a id="insn-006accb4"></a> `006accb4` | `60 02 40 b9` | ldr w0,[x19] | `FALL_THROUGH`
<a id="insn-006accb8"></a> `006accb8` | `b4 02 40 b9` | ldr w20,[x21] | `FALL_THROUGH`
<a id="insn-006accbc"></a> `006accbc` | `9b 47 fe 97` | bl 0x0063eb28 | `UNCONDITIONAL_CALL`
<a id="insn-006accc0"></a> `006accc0` | `9f 02 00 6b` | cmp w20,w0 | `FALL_THROUGH`
<a id="insn-006accc4"></a> `006accc4` | `0c ff ff 54` | b.gt 0x006acca4 | `CONDITIONAL_JUMP`
<a id="insn-006accc8"></a> `006accc8` | `60 5e 42 a9` | ldp x0,x23,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-006acccc"></a> `006acccc` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-006accd0"></a> `006accd0` | `e8 02 00 cb` | sub x8,x23,x0 | `FALL_THROUGH`
<a id="insn-006accd4"></a> `006accd4` | `02 fd 42 93` | asr x2,x8,#0x2 | `FALL_THROUGH`
<a id="insn-006accd8"></a> `006accd8` | `4a ba 14 94` | bl 0x00bdb600 | `UNCONDITIONAL_CALL`
<a id="insn-006accdc"></a> `006accdc` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-006acce0"></a> `006acce0` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-006acce4"></a> `006acce4` | `e9 02 80 9a` | csel x9,x23,x0,eq | `FALL_THROUGH`
<a id="insn-006acce8"></a> `006acce8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-006accec"></a> `006accec` | `c1 fd ff 54` | b.ne 0x006acca4 | `CONDITIONAL_JUMP`
<a id="insn-006accf0"></a> `006accf0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-006accf4"></a> `006accf4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006accf8"></a> `006accf8` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006accfc"></a> `006accfc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006acd00"></a> `006acd00` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006acd04"></a> `006acd04` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-006acd08"></a> `006acd08` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006acaac`](#insn-006acaac) 範囲 `[['006acaac', '006acaf7']]`
  - `CONDITIONAL_JUMP` [`006acaf4`](#insn-006acaf4) → [`006acb60`](#insn-006acb60)
  - `FALL_THROUGH` [`006acaf4`](#insn-006acaf4) → [`006acaf8`](#insn-006acaf8)
- ブロック [`006acaf8`](#insn-006acaf8) 範囲 `[['006acaf8', '006acb03']]`
  - `CONDITIONAL_JUMP` [`006acb00`](#insn-006acb00) → [`006acb64`](#insn-006acb64)
  - `FALL_THROUGH` [`006acb00`](#insn-006acb00) → [`006acb04`](#insn-006acb04)
- ブロック [`006acb04`](#insn-006acb04) 範囲 `[['006acb04', '006acb0f']]`
  - `CONDITIONAL_JUMP` [`006acb0c`](#insn-006acb0c) → [`006acb20`](#insn-006acb20)
  - `FALL_THROUGH` [`006acb0c`](#insn-006acb0c) → [`006acb10`](#insn-006acb10)
- ブロック [`006acb10`](#insn-006acb10) 範囲 `[['006acb10', '006acb13']]`
  - `UNCONDITIONAL_JUMP` [`006acb10`](#insn-006acb10) → [`006accf0`](#insn-006accf0)
- ブロック [`006acb14`](#insn-006acb14) 範囲 `[['006acb14', '006acb1f']]`
  - `CONDITIONAL_JUMP` [`006acb1c`](#insn-006acb1c) → [`006accf0`](#insn-006accf0)
  - `FALL_THROUGH` [`006acb1c`](#insn-006acb1c) → [`006acb20`](#insn-006acb20)
- ブロック [`006acb20`](#insn-006acb20) 範囲 `[['006acb20', '006acb33']]`
  - `CONDITIONAL_JUMP` [`006acb30`](#insn-006acb30) → [`006acb14`](#insn-006acb14)
  - `FALL_THROUGH` [`006acb30`](#insn-006acb30) → [`006acb34`](#insn-006acb34)
- ブロック [`006acb34`](#insn-006acb34) 範囲 `[['006acb34', '006acb5b']]`
  - `CONDITIONAL_JUMP` [`006acb58`](#insn-006acb58) → [`006acb14`](#insn-006acb14)
  - `FALL_THROUGH` [`006acb58`](#insn-006acb58) → [`006acb5c`](#insn-006acb5c)
- ブロック [`006acb5c`](#insn-006acb5c) 範囲 `[['006acb5c', '006acb5f']]`
  - `UNCONDITIONAL_JUMP` [`006acb5c`](#insn-006acb5c) → [`006acb64`](#insn-006acb64)
- ブロック [`006acb60`](#insn-006acb60) 範囲 `[['006acb60', '006acb63']]`
  - `FALL_THROUGH` [`006acb60`](#insn-006acb60) → [`006acb64`](#insn-006acb64)
- ブロック [`006acb64`](#insn-006acb64) 範囲 `[['006acb64', '006acb6f']]`
  - `CONDITIONAL_JUMP` [`006acb6c`](#insn-006acb6c) → [`006acbcc`](#insn-006acbcc)
  - `FALL_THROUGH` [`006acb6c`](#insn-006acb6c) → [`006acb70`](#insn-006acb70)
- ブロック [`006acb70`](#insn-006acb70) 範囲 `[['006acb70', '006acb7b']]`
  - `UNCONDITIONAL_JUMP` [`006acb78`](#insn-006acb78) → [`006acb80`](#insn-006acb80)
- ブロック [`006acb7c`](#insn-006acb7c) 範囲 `[['006acb7c', '006acb7f']]`
  - `FALL_THROUGH` [`006acb7c`](#insn-006acb7c) → [`006acb80`](#insn-006acb80)
- ブロック [`006acb80`](#insn-006acb80) 範囲 `[['006acb80', '006acb87']]`
  - `CONDITIONAL_JUMP` [`006acb84`](#insn-006acb84) → [`006acbd0`](#insn-006acbd0)
  - `FALL_THROUGH` [`006acb84`](#insn-006acb84) → [`006acb88`](#insn-006acb88)
- ブロック [`006acb88`](#insn-006acb88) 範囲 `[['006acb88', '006acb9b']]`
  - `CONDITIONAL_JUMP` [`006acb98`](#insn-006acb98) → [`006acb7c`](#insn-006acb7c)
  - `FALL_THROUGH` [`006acb98`](#insn-006acb98) → [`006acb9c`](#insn-006acb9c)
- ブロック [`006acb9c`](#insn-006acb9c) 範囲 `[['006acb9c', '006acbcb']]`
  - `UNCONDITIONAL_JUMP` [`006acbc8`](#insn-006acbc8) → [`006acb7c`](#insn-006acb7c)
- ブロック [`006acbcc`](#insn-006acbcc) 範囲 `[['006acbcc', '006acbcf']]`
  - `FALL_THROUGH` [`006acbcc`](#insn-006acbcc) → [`006acbd0`](#insn-006acbd0)
- ブロック [`006acbd0`](#insn-006acbd0) 範囲 `[['006acbd0', '006acbdb']]`
  - `CONDITIONAL_JUMP` [`006acbd8`](#insn-006acbd8) → [`006acc54`](#insn-006acc54)
  - `FALL_THROUGH` [`006acbd8`](#insn-006acbd8) → [`006acbdc`](#insn-006acbdc)
- ブロック [`006acbdc`](#insn-006acbdc) 範囲 `[['006acbdc', '006acbe3']]`
  - `UNCONDITIONAL_JUMP` [`006acbe0`](#insn-006acbe0) → [`006acbf4`](#insn-006acbf4)
- ブロック [`006acbe4`](#insn-006acbe4) 範囲 `[['006acbe4', '006acbe7']]`
  - `FALL_THROUGH` [`006acbe4`](#insn-006acbe4) → [`006acbe8`](#insn-006acbe8)
- ブロック [`006acbe8`](#insn-006acbe8) 範囲 `[['006acbe8', '006acbf3']]`
  - `CONDITIONAL_JUMP` [`006acbf0`](#insn-006acbf0) → [`006acc48`](#insn-006acc48)
  - `FALL_THROUGH` [`006acbf0`](#insn-006acbf0) → [`006acbf4`](#insn-006acbf4)
- ブロック [`006acbf4`](#insn-006acbf4) 範囲 `[['006acbf4', '006acc07']]`
  - `CONDITIONAL_JUMP` [`006acc04`](#insn-006acc04) → [`006acbe8`](#insn-006acbe8)
  - `FALL_THROUGH` [`006acc04`](#insn-006acc04) → [`006acc08`](#insn-006acc08)
- ブロック [`006acc08`](#insn-006acc08) 範囲 `[['006acc08', '006acc0f']]`
  - `CONDITIONAL_JUMP` [`006acc0c`](#insn-006acc0c) → [`006acbe4`](#insn-006acbe4)
  - `FALL_THROUGH` [`006acc0c`](#insn-006acc0c) → [`006acc10`](#insn-006acc10)
- ブロック [`006acc10`](#insn-006acc10) 範囲 `[['006acc10', '006acc13']]`
  - `CONDITIONAL_JUMP` [`006acc10`](#insn-006acc10) → [`006accf0`](#insn-006accf0)
  - `FALL_THROUGH` [`006acc10`](#insn-006acc10) → [`006acc14`](#insn-006acc14)
- ブロック [`006acc14`](#insn-006acc14) 範囲 `[['006acc14', '006acc1f']]`
  - `CONDITIONAL_JUMP` [`006acc1c`](#insn-006acc1c) → [`006accf0`](#insn-006accf0)
  - `FALL_THROUGH` [`006acc1c`](#insn-006acc1c) → [`006acc20`](#insn-006acc20)
- ブロック [`006acc20`](#insn-006acc20) 範囲 `[['006acc20', '006acc43']]`
  - `CONDITIONAL_JUMP` [`006acc40`](#insn-006acc40) → [`006acbe4`](#insn-006acbe4)
  - `FALL_THROUGH` [`006acc40`](#insn-006acc40) → [`006acc44`](#insn-006acc44)
- ブロック [`006acc44`](#insn-006acc44) 範囲 `[['006acc44', '006acc47']]`
  - `UNCONDITIONAL_JUMP` [`006acc44`](#insn-006acc44) → [`006accf0`](#insn-006accf0)
- ブロック [`006acc48`](#insn-006acc48) 範囲 `[['006acc48', '006acc4b']]`
  - `CONDITIONAL_JUMP` [`006acc48`](#insn-006acc48) → [`006acc54`](#insn-006acc54)
  - `FALL_THROUGH` [`006acc48`](#insn-006acc48) → [`006acc4c`](#insn-006acc4c)
- ブロック [`006acc4c`](#insn-006acc4c) 範囲 `[['006acc4c', '006acc53']]`
  - `UNCONDITIONAL_JUMP` [`006acc50`](#insn-006acc50) → [`006accf4`](#insn-006accf4)
- ブロック [`006acc54`](#insn-006acc54) 範囲 `[['006acc54', '006acc6b']]`
  - `CONDITIONAL_JUMP` [`006acc68`](#insn-006acc68) → [`006accf0`](#insn-006accf0)
  - `FALL_THROUGH` [`006acc68`](#insn-006acc68) → [`006acc6c`](#insn-006acc6c)
- ブロック [`006acc6c`](#insn-006acc6c) 範囲 `[['006acc6c', '006acc7f']]`
  - `CONDITIONAL_JUMP` [`006acc7c`](#insn-006acc7c) → [`006accf4`](#insn-006accf4)
  - `FALL_THROUGH` [`006acc7c`](#insn-006acc7c) → [`006acc80`](#insn-006acc80)
- ブロック [`006acc80`](#insn-006acc80) 範囲 `[['006acc80', '006acc87']]`
  - `CONDITIONAL_JUMP` [`006acc84`](#insn-006acc84) → [`006accf4`](#insn-006accf4)
  - `FALL_THROUGH` [`006acc84`](#insn-006acc84) → [`006acc88`](#insn-006acc88)
- ブロック [`006acc88`](#insn-006acc88) 範囲 `[['006acc88', '006acc93']]`
  - `CONDITIONAL_JUMP` [`006acc90`](#insn-006acc90) → [`006accf0`](#insn-006accf0)
  - `FALL_THROUGH` [`006acc90`](#insn-006acc90) → [`006acc94`](#insn-006acc94)
- ブロック [`006acc94`](#insn-006acc94) 範囲 `[['006acc94', '006acc9f']]`
  - `CONDITIONAL_JUMP` [`006acc9c`](#insn-006acc9c) → [`006accb4`](#insn-006accb4)
  - `FALL_THROUGH` [`006acc9c`](#insn-006acc9c) → [`006acca0`](#insn-006acca0)
- ブロック [`006acca0`](#insn-006acca0) 範囲 `[['006acca0', '006acca3']]`
  - `UNCONDITIONAL_JUMP` [`006acca0`](#insn-006acca0) → [`006acc4c`](#insn-006acc4c)
- ブロック [`006acca4`](#insn-006acca4) 範囲 `[['006acca4', '006accb3']]`
  - `CONDITIONAL_JUMP` [`006accb0`](#insn-006accb0) → [`006accf4`](#insn-006accf4)
  - `FALL_THROUGH` [`006accb0`](#insn-006accb0) → [`006accb4`](#insn-006accb4)
- ブロック [`006accb4`](#insn-006accb4) 範囲 `[['006accb4', '006accc7']]`
  - `CONDITIONAL_JUMP` [`006accc4`](#insn-006accc4) → [`006acca4`](#insn-006acca4)
  - `FALL_THROUGH` [`006accc4`](#insn-006accc4) → [`006accc8`](#insn-006accc8)
- ブロック [`006accc8`](#insn-006accc8) 範囲 `[['006accc8', '006accef']]`
  - `CONDITIONAL_JUMP` [`006accec`](#insn-006accec) → [`006acca4`](#insn-006acca4)
  - `FALL_THROUGH` [`006accec`](#insn-006accec) → [`006accf0`](#insn-006accf0)
- ブロック [`006accf0`](#insn-006accf0) 範囲 `[['006accf0', '006accf3']]`
  - `FALL_THROUGH` [`006accf0`](#insn-006accf0) → [`006accf4`](#insn-006accf4)
- ブロック [`006accf4`](#insn-006accf4) 範囲 `[['006accf4', '006acd0b']]`

## 命令位置別の参照

- [`006acaac`](#insn-006acaac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acab0`](#insn-006acab0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acab4`](#insn-006acab4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acab8`](#insn-006acab8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acabc`](#insn-006acabc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acac8`](#insn-006acac8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006acae0`](#insn-006acae0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006acaec`](#insn-006acaec) → `0032ff0c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[35]`
- [`006acaf4`](#insn-006acaf4) → [`006acb60`](#insn-006acb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb00`](#insn-006acb00) → [`006acb64`](#insn-006acb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb0c`](#insn-006acb0c) → [`006acb20`](#insn-006acb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb10`](#insn-006acb10) → [`006accf0`](#insn-006accf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb1c`](#insn-006acb1c) → [`006accf0`](#insn-006accf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb28`](#insn-006acb28) → [`0063eb28`](../0063e/0063eb28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0063eb28` · 推定シンボル `None` · 推定型 `None`
- [`006acb30`](#insn-006acb30) → [`006acb14`](#insn-006acb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb44`](#insn-006acb44) → [`00bdb600`](../00bdb/00bdb600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb600` · 推定シンボル `None` · 推定型 `None`
- [`006acb58`](#insn-006acb58) → [`006acb14`](#insn-006acb14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb5c`](#insn-006acb5c) → [`006acb64`](#insn-006acb64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb6c`](#insn-006acb6c) → [`006acbcc`](#insn-006acbcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb78`](#insn-006acb78) → [`006acb80`](#insn-006acb80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb84`](#insn-006acb84) → [`006acbd0`](#insn-006acbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb90`](#insn-006acb90) → [`0063eb28`](../0063e/0063eb28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0063eb28` · 推定シンボル `None` · 推定型 `None`
- [`006acb98`](#insn-006acb98) → [`006acb7c`](#insn-006acb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acbac`](#insn-006acbac) → [`00bdb600`](../00bdb/00bdb600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb600` · 推定シンボル `None` · 推定型 `None`
- [`006acbc8`](#insn-006acbc8) → [`006acb7c`](#insn-006acb7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acbd8`](#insn-006acbd8) → [`006acc54`](#insn-006acc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acbe0`](#insn-006acbe0) → [`006acbf4`](#insn-006acbf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acbf0`](#insn-006acbf0) → [`006acc48`](#insn-006acc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acbfc`](#insn-006acbfc) → [`0063eb28`](../0063e/0063eb28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0063eb28` · 推定シンボル `None` · 推定型 `None`
- [`006acc04`](#insn-006acc04) → [`006acbe8`](#insn-006acbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc0c`](#insn-006acc0c) → [`006acbe4`](#insn-006acbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc10`](#insn-006acc10) → [`006accf0`](#insn-006accf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc1c`](#insn-006acc1c) → [`006accf0`](#insn-006accf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc2c`](#insn-006acc2c) → [`00bdb600`](../00bdb/00bdb600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb600` · 推定シンボル `None` · 推定型 `None`
- [`006acc40`](#insn-006acc40) → [`006acbe4`](#insn-006acbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc44`](#insn-006acc44) → [`006accf0`](#insn-006accf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc48`](#insn-006acc48) → [`006acc54`](#insn-006acc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc50`](#insn-006acc50) → [`006accf4`](#insn-006accf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc54`](#insn-006acc54) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`006acc60`](#insn-006acc60) → `0032ff0c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[35]`
- [`006acc68`](#insn-006acc68) → [`006accf0`](#insn-006accf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc70`](#insn-006acc70) → [`0063eb28`](../0063e/0063eb28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0063eb28` · 推定シンボル `None` · 推定型 `None`
- [`006acc7c`](#insn-006acc7c) → [`006accf4`](#insn-006accf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc84`](#insn-006acc84) → [`006accf4`](#insn-006accf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc90`](#insn-006acc90) → [`006accf0`](#insn-006accf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acc9c`](#insn-006acc9c) → [`006accb4`](#insn-006accb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acca0`](#insn-006acca0) → [`006acc4c`](#insn-006acc4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006accb0`](#insn-006accb0) → [`006accf4`](#insn-006accf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006accbc`](#insn-006accbc) → [`0063eb28`](../0063e/0063eb28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0063eb28` · 推定シンボル `None` · 推定型 `None`
- [`006accc4`](#insn-006accc4) → [`006acca4`](#insn-006acca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006accd8`](#insn-006accd8) → [`00bdb600`](../00bdb/00bdb600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb600` · 推定シンボル `None` · 推定型 `None`
- [`006accec`](#insn-006accec) → [`006acca4`](#insn-006acca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006accf4`](#insn-006accf4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006accf8`](#insn-006accf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006accfc`](#insn-006accfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd00`](#insn-006acd00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd04`](#insn-006acd04) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006acaac`](#insn-006acaac)

~~~json
{
  "source": "006acaac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acab0`](#insn-006acab0)

~~~json
{
  "source": "006acab0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acab4`](#insn-006acab4)

~~~json
{
  "source": "006acab4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acab8`](#insn-006acab8)

~~~json
{
  "source": "006acab8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acabc`](#insn-006acabc)

~~~json
{
  "source": "006acabc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acac8`](#insn-006acac8)

~~~json
{
  "source": "006acac8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acae0`](#insn-006acae0)

~~~json
{
  "source": "006acae0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acaec`](#insn-006acaec)

~~~json
{
  "source": "006acaec",
  "target": "0032ff0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fef1",
  "offset": 27,
  "size": 35,
  "datatype": "byte[35]",
  "bytes": "440e304c0c1d2093049e069d0805480a05490c02500c1f304c0e00d3dedd0648",
  "capture_start": "0032fef1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006acaf4`](#insn-006acaf4)

~~~json
{
  "source": "006acaf4",
  "target": "006acb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb00`](#insn-006acb00)

~~~json
{
  "source": "006acb00",
  "target": "006acb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb0c`](#insn-006acb0c)

~~~json
{
  "source": "006acb0c",
  "target": "006acb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb10`](#insn-006acb10)

~~~json
{
  "source": "006acb10",
  "target": "006accf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb1c`](#insn-006acb1c)

~~~json
{
  "source": "006acb1c",
  "target": "006accf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb28`](#insn-006acb28)

~~~json
{
  "source": "006acb28",
  "target": "0063eb28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb30`](#insn-006acb30)

~~~json
{
  "source": "006acb30",
  "target": "006acb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb44`](#insn-006acb44)

~~~json
{
  "source": "006acb44",
  "target": "00bdb600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb58`](#insn-006acb58)

~~~json
{
  "source": "006acb58",
  "target": "006acb14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb5c`](#insn-006acb5c)

~~~json
{
  "source": "006acb5c",
  "target": "006acb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb6c`](#insn-006acb6c)

~~~json
{
  "source": "006acb6c",
  "target": "006acbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb78`](#insn-006acb78)

~~~json
{
  "source": "006acb78",
  "target": "006acb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb84`](#insn-006acb84)

~~~json
{
  "source": "006acb84",
  "target": "006acbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb90`](#insn-006acb90)

~~~json
{
  "source": "006acb90",
  "target": "0063eb28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb98`](#insn-006acb98)

~~~json
{
  "source": "006acb98",
  "target": "006acb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acbac`](#insn-006acbac)

~~~json
{
  "source": "006acbac",
  "target": "00bdb600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbc8`](#insn-006acbc8)

~~~json
{
  "source": "006acbc8",
  "target": "006acb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acbd8`](#insn-006acbd8)

~~~json
{
  "source": "006acbd8",
  "target": "006acc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acbe0`](#insn-006acbe0)

~~~json
{
  "source": "006acbe0",
  "target": "006acbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acbf0`](#insn-006acbf0)

~~~json
{
  "source": "006acbf0",
  "target": "006acc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acbfc`](#insn-006acbfc)

~~~json
{
  "source": "006acbfc",
  "target": "0063eb28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc04`](#insn-006acc04)

~~~json
{
  "source": "006acc04",
  "target": "006acbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc0c`](#insn-006acc0c)

~~~json
{
  "source": "006acc0c",
  "target": "006acbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc10`](#insn-006acc10)

~~~json
{
  "source": "006acc10",
  "target": "006accf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc1c`](#insn-006acc1c)

~~~json
{
  "source": "006acc1c",
  "target": "006accf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc2c`](#insn-006acc2c)

~~~json
{
  "source": "006acc2c",
  "target": "00bdb600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc40`](#insn-006acc40)

~~~json
{
  "source": "006acc40",
  "target": "006acbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc44`](#insn-006acc44)

~~~json
{
  "source": "006acc44",
  "target": "006accf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc48`](#insn-006acc48)

~~~json
{
  "source": "006acc48",
  "target": "006acc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc50`](#insn-006acc50)

~~~json
{
  "source": "006acc50",
  "target": "006accf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc54`](#insn-006acc54)

~~~json
{
  "source": "006acc54",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc60`](#insn-006acc60)

~~~json
{
  "source": "006acc60",
  "target": "0032ff0c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0032fef1",
  "offset": 27,
  "size": 35,
  "datatype": "byte[35]",
  "bytes": "440e304c0c1d2093049e069d0805480a05490c02500c1f304c0e00d3dedd0648",
  "capture_start": "0032fef1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006acc68`](#insn-006acc68)

~~~json
{
  "source": "006acc68",
  "target": "006accf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc70`](#insn-006acc70)

~~~json
{
  "source": "006acc70",
  "target": "0063eb28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc7c`](#insn-006acc7c)

~~~json
{
  "source": "006acc7c",
  "target": "006accf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc84`](#insn-006acc84)

~~~json
{
  "source": "006acc84",
  "target": "006accf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc90`](#insn-006acc90)

~~~json
{
  "source": "006acc90",
  "target": "006accf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acc9c`](#insn-006acc9c)

~~~json
{
  "source": "006acc9c",
  "target": "006accb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acca0`](#insn-006acca0)

~~~json
{
  "source": "006acca0",
  "target": "006acc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006accb0`](#insn-006accb0)

~~~json
{
  "source": "006accb0",
  "target": "006accf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006accbc`](#insn-006accbc)

~~~json
{
  "source": "006accbc",
  "target": "0063eb28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006accc4`](#insn-006accc4)

~~~json
{
  "source": "006accc4",
  "target": "006acca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006accd8`](#insn-006accd8)

~~~json
{
  "source": "006accd8",
  "target": "00bdb600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006accec`](#insn-006accec)

~~~json
{
  "source": "006accec",
  "target": "006acca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006accf4`](#insn-006accf4)

~~~json
{
  "source": "006accf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006accf8`](#insn-006accf8)

~~~json
{
  "source": "006accf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006accfc`](#insn-006accfc)

~~~json
{
  "source": "006accfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd00`](#insn-006acd00)

~~~json
{
  "source": "006acd00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd04`](#insn-006acd04)

~~~json
{
  "source": "006acd04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
