# 00bd4bdc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd4b98`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4b98.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0019.md#compare-65e0d4d3c23c42a1eba104fd2432fe73)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c51624`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c51/00c51624.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0078.md#compare-0d7af9423babf68be3202f120887c2d9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd4bdc",
  "name": "FUN_00bd4bdc",
  "size": 272,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "570edd918c2461921137c50411a4b489531290bbcf8934cf488ade53c52030b3",
  "source_text_sha256": "570edd918c2461921137c50411a4b489531290bbcf8934cf488ade53c52030b3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd4bdc",
        "00bd4ceb"
      ]
    ],
    "bytes_sha256": "65282579d14682488e6604b147c3537990fd6d61ec0c1f793f4e22f655f70af8",
    "instruction_count": 68,
    "instruction_bytes": 272,
    "body_bytes": 272,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bd4d04](../00bd4/00bd4d04.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2418 bytes

~~~c

void FUN_00bd4bdc(long param_1,undefined8 *param_2)

{
  ushort uVar1;
  ushort uVar2;
  ulong uVar3;
  void *__ptr;
  long *extraout_x1;
  long lVar4;
  size_t __size;
  
  if ((*(byte *)(param_1 + 0x1c) & 1) != 0) {
    return;
  }
                    /* catch(type#1 @ 00000000) { ... } // from try @ 00bd4af8 with catch @ 00bd4bf8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bd4b28 with catch @ 00bd4bf8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bd4b5c with catch @ 00bd4bf8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bd4b88 with catch @ 00bd4bf8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bd4bb0 with catch @ 00bd4bf8
                        */
                    /* try { // try from 00bd4bfc to 00cd4cff has its CatchHandler @ 00bd4bfc
                       catch() { ... } // from try @ 00bd4bfc with catch @ 00bd4bfc
                       catch() { ... } // from try @ 00bd4d08 with catch @ 00bd4bfc
                       catch() { ... } // from try @ 00bd4dbc with catch @ 00bd4bfc */
  *(undefined1 *)(param_1 + 0x1c) = 1;
  FUN_00bd4d04();
  if (extraout_x1 == (long *)0x0) goto LAB_00bd4cd0;
  uVar1 = *(ushort *)((long)extraout_x1 + 9);
  uVar2 = uVar1 >> 8 & 3;
  if (uVar2 == 0) {
LAB_00bd4c70:
    lVar4 = param_2[1];
    __ptr = (void *)*param_2;
    if ((ulong)param_2[2] < lVar4 + 1U) {
      __size = param_2[2] * 2;
      uVar3 = lVar4 + 0x3e1;
      if (__size < uVar3 || __size - uVar3 == 0) {
        __size = uVar3;
      }
      param_2[2] = __size;
      __ptr = realloc(__ptr,__size);
      *param_2 = __ptr;
      if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar4 = param_2[1];
    }
    *(undefined1 *)((long)__ptr + lVar4) = 0x29;
    param_2[1] = param_2[1] + 1;
  }
  else {
    if (uVar2 == 2) {
      uVar3 = (**(code **)(*extraout_x1 + 8))(extraout_x1,param_2);
      if ((uVar3 & 1) != 0) goto LAB_00bd4c70;
      uVar1 = *(ushort *)((long)extraout_x1 + 9);
    }
    if (((uVar1 >> 10 & 3) == 0) ||
       (((uVar1 >> 10 & 3) == 2 &&
        (uVar3 = (**(code **)(*extraout_x1 + 0x10))(extraout_x1,param_2), (uVar3 & 1) != 0))))
    goto LAB_00bd4c70;
  }
  (**(code **)(*extraout_x1 + 0x28))(extraout_x1,param_2);
LAB_00bd4cd0:
  *(undefined1 *)(param_1 + 0x1c) = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd4bdc"></a> `00bd4bdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd4be0"></a> `00bd4be0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bd4be4"></a> `00bd4be4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd4be8"></a> `00bd4be8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd4bec"></a> `00bd4bec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bd4bf0"></a> `00bd4bf0` | `08 70 40 39` | ldrb w8,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00bd4bf4"></a> `00bd4bf4` | `08 07 00 37` | tbnz w8,#0x0,0x00bd4cd4 | `CONDITIONAL_JUMP`
<a id="insn-00bd4bf8"></a> `00bd4bf8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bd4bfc"></a> `00bd4bfc` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd4c00"></a> `00bd4c00` | `08 70 00 39` | strb w8,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00bd4c04"></a> `00bd4c04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd4c08"></a> `00bd4c08` | `3f 00 00 94` | bl 0x00bd4d04 | `UNCONDITIONAL_CALL`
<a id="insn-00bd4c0c"></a> `00bd4c0c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bd4c10"></a> `00bd4c10` | `01 06 00 b4` | cbz x1,0x00bd4cd0 | `CONDITIONAL_JUMP`
<a id="insn-00bd4c14"></a> `00bd4c14` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd4c18"></a> `00bd4c18` | `09 25 08 53` | ubfx w9,w8,#0x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bd4c1c"></a> `00bd4c1c` | `a9 02 00 34` | cbz w9,0x00bd4c70 | `CONDITIONAL_JUMP`
<a id="insn-00bd4c20"></a> `00bd4c20` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bd4c24"></a> `00bd4c24` | `01 01 00 54` | b.ne 0x00bd4c44 | `CONDITIONAL_JUMP`
<a id="insn-00bd4c28"></a> `00bd4c28` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd4c2c"></a> `00bd4c2c` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bd4c30"></a> `00bd4c30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd4c34"></a> `00bd4c34` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd4c38"></a> `00bd4c38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4c3c"></a> `00bd4c3c` | `a0 01 00 37` | tbnz w0,#0x0,0x00bd4c70 | `CONDITIONAL_JUMP`
<a id="insn-00bd4c40"></a> `00bd4c40` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd4c44"></a> `00bd4c44` | `08 7d 0a 53` | lsr w8,w8,#0xa | `FALL_THROUGH`
<a id="insn-00bd4c48"></a> `00bd4c48` | `08 05 00 72` | ands w8,w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bd4c4c"></a> `00bd4c4c` | `20 01 00 54` | b.eq 0x00bd4c70 | `CONDITIONAL_JUMP`
<a id="insn-00bd4c50"></a> `00bd4c50` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bd4c54"></a> `00bd4c54` | `41 03 00 54` | b.ne 0x00bd4cbc | `CONDITIONAL_JUMP`
<a id="insn-00bd4c58"></a> `00bd4c58` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd4c5c"></a> `00bd4c5c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bd4c60"></a> `00bd4c60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd4c64"></a> `00bd4c64` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd4c68"></a> `00bd4c68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4c6c"></a> `00bd4c6c` | `80 02 00 36` | tbz w0,#0x0,0x00bd4cbc | `CONDITIONAL_JUMP`
<a id="insn-00bd4c70"></a> `00bd4c70` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd4c74"></a> `00bd4c74` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd4c78"></a> `00bd4c78` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd4c7c"></a> `00bd4c7c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd4c80"></a> `00bd4c80` | `49 01 00 54` | b.ls 0x00bd4ca8 | `CONDITIONAL_JUMP`
<a id="insn-00bd4c84"></a> `00bd4c84` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd4c88"></a> `00bd4c88` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bd4c8c"></a> `00bd4c8c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd4c90"></a> `00bd4c90` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd4c94"></a> `00bd4c94` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd4c98"></a> `00bd4c98` | `6e 21 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bd4c9c"></a> `00bd4c9c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd4ca0"></a> `00bd4ca0` | `40 02 00 b4` | cbz x0,0x00bd4ce8 | `CONDITIONAL_JUMP`
<a id="insn-00bd4ca4"></a> `00bd4ca4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd4ca8"></a> `00bd4ca8` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00bd4cac"></a> `00bd4cac` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bd4cb0"></a> `00bd4cb0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd4cb4"></a> `00bd4cb4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd4cb8"></a> `00bd4cb8` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd4cbc"></a> `00bd4cbc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd4cc0"></a> `00bd4cc0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd4cc4"></a> `00bd4cc4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd4cc8"></a> `00bd4cc8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd4ccc"></a> `00bd4ccc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd4cd0"></a> `00bd4cd0` | `bf 72 00 39` | strb wzr,[x21, #0x1c] | `FALL_THROUGH`
<a id="insn-00bd4cd4"></a> `00bd4cd4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd4cd8"></a> `00bd4cd8` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd4cdc"></a> `00bd4cdc` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd4ce0"></a> `00bd4ce0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd4ce4"></a> `00bd4ce4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd4ce8"></a> `00bd4ce8` | `76 25 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd4bdc`](#insn-00bd4bdc) 範囲 `[['00bd4bdc', '00bd4bf7']]`
  - `CONDITIONAL_JUMP` [`00bd4bf4`](#insn-00bd4bf4) → [`00bd4cd4`](#insn-00bd4cd4)
  - `FALL_THROUGH` [`00bd4bf4`](#insn-00bd4bf4) → [`00bd4bf8`](#insn-00bd4bf8)
- ブロック [`00bd4bf8`](#insn-00bd4bf8) 範囲 `[['00bd4bf8', '00bd4bfb']]`
  - `FALL_THROUGH` [`00bd4bf8`](#insn-00bd4bf8) → [`00bd4bfc`](#insn-00bd4bfc)
- ブロック [`00bd4bfc`](#insn-00bd4bfc) 範囲 `[['00bd4bfc', '00bd4c13']]`
  - `CONDITIONAL_JUMP` [`00bd4c10`](#insn-00bd4c10) → [`00bd4cd0`](#insn-00bd4cd0)
  - `FALL_THROUGH` [`00bd4c10`](#insn-00bd4c10) → [`00bd4c14`](#insn-00bd4c14)
- ブロック [`00bd4c14`](#insn-00bd4c14) 範囲 `[['00bd4c14', '00bd4c1f']]`
  - `CONDITIONAL_JUMP` [`00bd4c1c`](#insn-00bd4c1c) → [`00bd4c70`](#insn-00bd4c70)
  - `FALL_THROUGH` [`00bd4c1c`](#insn-00bd4c1c) → [`00bd4c20`](#insn-00bd4c20)
- ブロック [`00bd4c20`](#insn-00bd4c20) 範囲 `[['00bd4c20', '00bd4c27']]`
  - `CONDITIONAL_JUMP` [`00bd4c24`](#insn-00bd4c24) → [`00bd4c44`](#insn-00bd4c44)
  - `FALL_THROUGH` [`00bd4c24`](#insn-00bd4c24) → [`00bd4c28`](#insn-00bd4c28)
- ブロック [`00bd4c28`](#insn-00bd4c28) 範囲 `[['00bd4c28', '00bd4c3f']]`
  - `CONDITIONAL_JUMP` [`00bd4c3c`](#insn-00bd4c3c) → [`00bd4c70`](#insn-00bd4c70)
  - `FALL_THROUGH` [`00bd4c3c`](#insn-00bd4c3c) → [`00bd4c40`](#insn-00bd4c40)
- ブロック [`00bd4c40`](#insn-00bd4c40) 範囲 `[['00bd4c40', '00bd4c43']]`
  - `FALL_THROUGH` [`00bd4c40`](#insn-00bd4c40) → [`00bd4c44`](#insn-00bd4c44)
- ブロック [`00bd4c44`](#insn-00bd4c44) 範囲 `[['00bd4c44', '00bd4c4f']]`
  - `CONDITIONAL_JUMP` [`00bd4c4c`](#insn-00bd4c4c) → [`00bd4c70`](#insn-00bd4c70)
  - `FALL_THROUGH` [`00bd4c4c`](#insn-00bd4c4c) → [`00bd4c50`](#insn-00bd4c50)
- ブロック [`00bd4c50`](#insn-00bd4c50) 範囲 `[['00bd4c50', '00bd4c57']]`
  - `CONDITIONAL_JUMP` [`00bd4c54`](#insn-00bd4c54) → [`00bd4cbc`](#insn-00bd4cbc)
  - `FALL_THROUGH` [`00bd4c54`](#insn-00bd4c54) → [`00bd4c58`](#insn-00bd4c58)
- ブロック [`00bd4c58`](#insn-00bd4c58) 範囲 `[['00bd4c58', '00bd4c6f']]`
  - `CONDITIONAL_JUMP` [`00bd4c6c`](#insn-00bd4c6c) → [`00bd4cbc`](#insn-00bd4cbc)
  - `FALL_THROUGH` [`00bd4c6c`](#insn-00bd4c6c) → [`00bd4c70`](#insn-00bd4c70)
- ブロック [`00bd4c70`](#insn-00bd4c70) 範囲 `[['00bd4c70', '00bd4c83']]`
  - `CONDITIONAL_JUMP` [`00bd4c80`](#insn-00bd4c80) → [`00bd4ca8`](#insn-00bd4ca8)
  - `FALL_THROUGH` [`00bd4c80`](#insn-00bd4c80) → [`00bd4c84`](#insn-00bd4c84)
- ブロック [`00bd4c84`](#insn-00bd4c84) 範囲 `[['00bd4c84', '00bd4ca3']]`
  - `CONDITIONAL_JUMP` [`00bd4ca0`](#insn-00bd4ca0) → [`00bd4ce8`](#insn-00bd4ce8)
  - `FALL_THROUGH` [`00bd4ca0`](#insn-00bd4ca0) → [`00bd4ca4`](#insn-00bd4ca4)
- ブロック [`00bd4ca4`](#insn-00bd4ca4) 範囲 `[['00bd4ca4', '00bd4ca7']]`
  - `FALL_THROUGH` [`00bd4ca4`](#insn-00bd4ca4) → [`00bd4ca8`](#insn-00bd4ca8)
- ブロック [`00bd4ca8`](#insn-00bd4ca8) 範囲 `[['00bd4ca8', '00bd4cbb']]`
  - `FALL_THROUGH` [`00bd4cb8`](#insn-00bd4cb8) → [`00bd4cbc`](#insn-00bd4cbc)
- ブロック [`00bd4cbc`](#insn-00bd4cbc) 範囲 `[['00bd4cbc', '00bd4ccf']]`
  - `FALL_THROUGH` [`00bd4ccc`](#insn-00bd4ccc) → [`00bd4cd0`](#insn-00bd4cd0)
- ブロック [`00bd4cd0`](#insn-00bd4cd0) 範囲 `[['00bd4cd0', '00bd4cd3']]`
  - `FALL_THROUGH` [`00bd4cd0`](#insn-00bd4cd0) → [`00bd4cd4`](#insn-00bd4cd4)
- ブロック [`00bd4cd4`](#insn-00bd4cd4) 範囲 `[['00bd4cd4', '00bd4ce7']]`
- ブロック [`00bd4ce8`](#insn-00bd4ce8) 範囲 `[['00bd4ce8', '00bd4ceb']]`

## 命令位置別の参照

- [`00bd4be0`](#insn-00bd4be0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4be4`](#insn-00bd4be4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4be8`](#insn-00bd4be8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4bf4`](#insn-00bd4bf4) → [`00bd4cd4`](#insn-00bd4cd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c08`](#insn-00bd4c08) → [`00bd4d04`](00bd4d04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd4d04` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c10`](#insn-00bd4c10) → [`00bd4cd0`](#insn-00bd4cd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c1c`](#insn-00bd4c1c) → [`00bd4c70`](#insn-00bd4c70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c24`](#insn-00bd4c24) → [`00bd4c44`](#insn-00bd4c44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c3c`](#insn-00bd4c3c) → [`00bd4c70`](#insn-00bd4c70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c4c`](#insn-00bd4c4c) → [`00bd4c70`](#insn-00bd4c70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c54`](#insn-00bd4c54) → [`00bd4cbc`](#insn-00bd4cbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c6c`](#insn-00bd4c6c) → [`00bd4cbc`](#insn-00bd4cbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c80`](#insn-00bd4c80) → [`00bd4ca8`](#insn-00bd4ca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4c98`](#insn-00bd4c98) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bd4ca0`](#insn-00bd4ca0) → [`00bd4ce8`](#insn-00bd4ce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4cd4`](#insn-00bd4cd4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4cd8`](#insn-00bd4cd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4cdc`](#insn-00bd4cdc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd4ce8`](#insn-00bd4ce8) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd4be0`](#insn-00bd4be0)

~~~json
{
  "source": "00bd4be0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4be4`](#insn-00bd4be4)

~~~json
{
  "source": "00bd4be4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4be8`](#insn-00bd4be8)

~~~json
{
  "source": "00bd4be8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4bf4`](#insn-00bd4bf4)

~~~json
{
  "source": "00bd4bf4",
  "target": "00bd4cd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c08`](#insn-00bd4c08)

~~~json
{
  "source": "00bd4c08",
  "target": "00bd4d04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4c10`](#insn-00bd4c10)

~~~json
{
  "source": "00bd4c10",
  "target": "00bd4cd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c1c`](#insn-00bd4c1c)

~~~json
{
  "source": "00bd4c1c",
  "target": "00bd4c70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c24`](#insn-00bd4c24)

~~~json
{
  "source": "00bd4c24",
  "target": "00bd4c44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c3c`](#insn-00bd4c3c)

~~~json
{
  "source": "00bd4c3c",
  "target": "00bd4c70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c4c`](#insn-00bd4c4c)

~~~json
{
  "source": "00bd4c4c",
  "target": "00bd4c70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c54`](#insn-00bd4c54)

~~~json
{
  "source": "00bd4c54",
  "target": "00bd4cbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c6c`](#insn-00bd4c6c)

~~~json
{
  "source": "00bd4c6c",
  "target": "00bd4cbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c80`](#insn-00bd4c80)

~~~json
{
  "source": "00bd4c80",
  "target": "00bd4ca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4c98`](#insn-00bd4c98)

~~~json
{
  "source": "00bd4c98",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd4ca0`](#insn-00bd4ca0)

~~~json
{
  "source": "00bd4ca0",
  "target": "00bd4ce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4cd4`](#insn-00bd4cd4)

~~~json
{
  "source": "00bd4cd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4cd8`](#insn-00bd4cd8)

~~~json
{
  "source": "00bd4cd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4cdc`](#insn-00bd4cdc)

~~~json
{
  "source": "00bd4cdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd4ce8`](#insn-00bd4ce8)

~~~json
{
  "source": "00bd4ce8",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
