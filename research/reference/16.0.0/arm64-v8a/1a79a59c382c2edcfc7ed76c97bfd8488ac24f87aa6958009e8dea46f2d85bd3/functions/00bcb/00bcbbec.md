# 00bcbbec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5c6ec`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c6ec.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-63edda289fcbeefba9e98193a1b61a35)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc014`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc014.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-08dbdc62423536205ad0a9e6e0ee1fc6)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbbec",
  "name": "_ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edc4b826f6c8a213f52cbd76638ebb4ff904c483d868c9fc8fd94dd91412267e",
  "source_text_sha256": "edc4b826f6c8a213f52cbd76638ebb4ff904c483d868c9fc8fd94dd91412267e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbbec",
        "00bcbce3"
      ]
    ],
    "bytes_sha256": "bb4f5d96cc2629f4fdbe8368934dcbb8715967b7dad41ee8512a4a46615b784d",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d6d0](../00c5d/00c5d6d0.md)

## 呼び出し先

- [00b3fe98](../00b3f/00b3fe98.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c5a910](../00c5a/00c5a910.md)

## 関連文字列（未確認候補）

~~~text
"allocator<T>::allocate(size_t n) 'n' exceeds maximum supported size"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1488 bytes

~~~c

void _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  void *__src;
  void *__dest;
  ulong uVar2;
  size_t __n;
  ulong uVar3;
  
  __src = (void *)*param_1;
  __n = param_1[1] - (long)__src;
  uVar3 = ((long)__n >> 3) + 1;
  if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
    _ZNKSt6__ndk120__vector_base_commonILb1EE20__throw_length_errorEv(param_1);
  }
  if ((ulong)(param_1[2] - (long)__src >> 3) < 0xfffffffffffffff) {
    uVar2 = param_1[2] - (long)__src >> 2;
    if (uVar3 <= uVar2) {
      uVar3 = uVar2;
    }
    if (uVar3 == 0) {
      __dest = (void *)0x0;
      goto LAB_00bcbc6c;
    }
    if (uVar3 >> 0x3d != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00b3fe98("allocator<T>::allocate(size_t n) \'n\' exceeds maximum supported size");
    }
  }
  else {
    uVar3 = 0x1fffffffffffffff;
  }
  __dest = (void *)_Znwm(uVar3 << 3);
LAB_00bcbc6c:
  puVar1 = (undefined8 *)((long)__dest + ((long)__n >> 3) * 8);
                    /* catch() { ... } // from try @ 00bcbb88 with catch @ 00bcbc7c */
  *puVar1 = *param_2;
  if (0 < (long)__n) {
    memcpy(__dest,__src,__n);
  }
  *param_1 = __dest;
  param_1[1] = puVar1 + 1;
  param_1[2] = (void *)((long)__dest + uVar3 * 8);
  if (__src != (void *)0x0) {
    _ZdlPv(__src);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbbec"></a> `00bcbbec` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcbbf0"></a> `00bcbbf0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbbf4"></a> `00bcbbf4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbf8"></a> `00bcbbf8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbbfc"></a> `00bcbbfc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbc00"></a> `00bcbc00` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcbc04"></a> `00bcbc04` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbc08"></a> `00bcbc08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbc0c"></a> `00bcbc0c` | `15 01 14 cb` | sub x21,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcbc10"></a> `00bcbc10` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbc14"></a> `00bcbc14` | `08 07 00 91` | add x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbc18"></a> `00bcbc18` | `09 fd 7d d3` | lsr x9,x8,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbc1c"></a> `00bcbc1c` | `09 06 00 b5` | cbnz x9,0x00bcbcdc | `CONDITIONAL_JUMP`
<a id="insn-00bcbc20"></a> `00bcbc20` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbc24"></a> `00bcbc24` | `ea eb 7f b2` | orr x10,xzr,#0xffffffffffffffe | `FALL_THROUGH`
<a id="insn-00bcbc28"></a> `00bcbc28` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bcbc2c"></a> `00bcbc2c` | `29 01 14 cb` | sub x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bcbc30"></a> `00bcbc30` | `5f 0d 89 eb` | cmp x10,x9, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bcbc34"></a> `00bcbc34` | `43 01 00 54` | b.cc 0x00bcbc5c | `CONDITIONAL_JUMP`
<a id="insn-00bcbc38"></a> `00bcbc38` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bcbc3c"></a> `00bcbc3c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbc40"></a> `00bcbc40` | `19 31 89 9a` | csel x25,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bcbc44"></a> `00bcbc44` | `99 04 00 b4` | cbz x25,0x00bcbcd4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc48"></a> `00bcbc48` | `28 ff 7d d3` | lsr x8,x25,#0x3d | `FALL_THROUGH`
<a id="insn-00bcbc4c"></a> `00bcbc4c` | `a8 00 00 b4` | cbz x8,0x00bcbc60 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc50"></a> `00bcbc50` | `e0 b6 ff b0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcbc54"></a> `00bcbc54` | `00 b8 16 91` | add x0,x0,#0x5ae | `FALL_THROUGH`
<a id="insn-00bcbc58"></a> `00bcbc58` | `90 d0 fd 97` | bl 0x00b3fe98 | `CALL_TERMINATOR`
<a id="insn-00bcbc5c"></a> `00bcbc5c` | `19 00 fc 92` | mov x25,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bcbc60"></a> `00bcbc60` | `20 f3 7d d3` | lsl x0,x25,#0x3 | `FALL_THROUGH`
<a id="insn-00bcbc64"></a> `00bcbc64` | `8b 2f 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc68"></a> `00bcbc68` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcbc6c"></a> `00bcbc6c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bcbc70"></a> `00bcbc70` | `f8 0e 18 8b` | add x24,x23,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcbc74"></a> `00bcbc74` | `f6 0e 19 8b` | add x22,x23,x25, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bcbc78"></a> `00bcbc78` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbc7c"></a> `00bcbc7c` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00bcbc80"></a> `00bcbc80` | `ab 00 00 54` | b.lt 0x00bcbc94 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc84"></a> `00bcbc84` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcbc88"></a> `00bcbc88` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcbc8c"></a> `00bcbc8c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00bcbc90"></a> `00bcbc90` | `dc 2f 02 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc94"></a> `00bcbc94` | `77 62 00 a9` | stp x23,x24,[x19] | `FALL_THROUGH`
<a id="insn-00bcbc98"></a> `00bcbc98` | `76 0a 00 f9` | str x22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbc9c"></a> `00bcbc9c` | `14 01 00 b4` | cbz x20,0x00bcbcbc | `CONDITIONAL_JUMP`
<a id="insn-00bcbca0"></a> `00bcbca0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcbca4"></a> `00bcbca4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbca8"></a> `00bcbca8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbcac"></a> `00bcbcac` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbcb0"></a> `00bcbcb0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbcb4"></a> `00bcbcb4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbcb8"></a> `00bcbcb8` | `7e 2f 02 14` | b 0x00c57ab0 | `CALL_TERMINATOR`
<a id="insn-00bcbcbc"></a> `00bcbcbc` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbcc0"></a> `00bcbcc0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbcc4"></a> `00bcbcc4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbcc8"></a> `00bcbcc8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbccc"></a> `00bcbccc` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcbcd0"></a> `00bcbcd0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbcd4"></a> `00bcbcd4` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bcbcd8"></a> `00bcbcd8` | `e5 ff ff 17` | b 0x00bcbc6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbcdc"></a> `00bcbcdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbce0"></a> `00bcbce0` | `0c 3b 02 94` | bl 0x00c5a910 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbbec`](#insn-00bcbbec) 範囲 `[['00bcbbec', '00bcbc1f']]`
  - `CONDITIONAL_JUMP` [`00bcbc1c`](#insn-00bcbc1c) → [`00bcbcdc`](#insn-00bcbcdc)
  - `FALL_THROUGH` [`00bcbc1c`](#insn-00bcbc1c) → [`00bcbc20`](#insn-00bcbc20)
- ブロック [`00bcbc20`](#insn-00bcbc20) 範囲 `[['00bcbc20', '00bcbc37']]`
  - `CONDITIONAL_JUMP` [`00bcbc34`](#insn-00bcbc34) → [`00bcbc5c`](#insn-00bcbc5c)
  - `FALL_THROUGH` [`00bcbc34`](#insn-00bcbc34) → [`00bcbc38`](#insn-00bcbc38)
- ブロック [`00bcbc38`](#insn-00bcbc38) 範囲 `[['00bcbc38', '00bcbc47']]`
  - `CONDITIONAL_JUMP` [`00bcbc44`](#insn-00bcbc44) → [`00bcbcd4`](#insn-00bcbcd4)
  - `FALL_THROUGH` [`00bcbc44`](#insn-00bcbc44) → [`00bcbc48`](#insn-00bcbc48)
- ブロック [`00bcbc48`](#insn-00bcbc48) 範囲 `[['00bcbc48', '00bcbc4f']]`
  - `CONDITIONAL_JUMP` [`00bcbc4c`](#insn-00bcbc4c) → [`00bcbc60`](#insn-00bcbc60)
  - `FALL_THROUGH` [`00bcbc4c`](#insn-00bcbc4c) → [`00bcbc50`](#insn-00bcbc50)
- ブロック [`00bcbc50`](#insn-00bcbc50) 範囲 `[['00bcbc50', '00bcbc5b']]`
- ブロック [`00bcbc5c`](#insn-00bcbc5c) 範囲 `[['00bcbc5c', '00bcbc5f']]`
  - `FALL_THROUGH` [`00bcbc5c`](#insn-00bcbc5c) → [`00bcbc60`](#insn-00bcbc60)
- ブロック [`00bcbc60`](#insn-00bcbc60) 範囲 `[['00bcbc60', '00bcbc6b']]`
  - `FALL_THROUGH` [`00bcbc68`](#insn-00bcbc68) → [`00bcbc6c`](#insn-00bcbc6c)
- ブロック [`00bcbc6c`](#insn-00bcbc6c) 範囲 `[['00bcbc6c', '00bcbc7b']]`
  - `FALL_THROUGH` [`00bcbc78`](#insn-00bcbc78) → [`00bcbc7c`](#insn-00bcbc7c)
- ブロック [`00bcbc7c`](#insn-00bcbc7c) 範囲 `[['00bcbc7c', '00bcbc83']]`
  - `CONDITIONAL_JUMP` [`00bcbc80`](#insn-00bcbc80) → [`00bcbc94`](#insn-00bcbc94)
  - `FALL_THROUGH` [`00bcbc80`](#insn-00bcbc80) → [`00bcbc84`](#insn-00bcbc84)
- ブロック [`00bcbc84`](#insn-00bcbc84) 範囲 `[['00bcbc84', '00bcbc93']]`
  - `FALL_THROUGH` [`00bcbc90`](#insn-00bcbc90) → [`00bcbc94`](#insn-00bcbc94)
- ブロック [`00bcbc94`](#insn-00bcbc94) 範囲 `[['00bcbc94', '00bcbc9f']]`
  - `CONDITIONAL_JUMP` [`00bcbc9c`](#insn-00bcbc9c) → [`00bcbcbc`](#insn-00bcbcbc)
  - `FALL_THROUGH` [`00bcbc9c`](#insn-00bcbc9c) → [`00bcbca0`](#insn-00bcbca0)
- ブロック [`00bcbca0`](#insn-00bcbca0) 範囲 `[['00bcbca0', '00bcbcbb']]`
- ブロック [`00bcbcbc`](#insn-00bcbcbc) 範囲 `[['00bcbcbc', '00bcbcd3']]`
- ブロック [`00bcbcd4`](#insn-00bcbcd4) 範囲 `[['00bcbcd4', '00bcbcdb']]`
  - `UNCONDITIONAL_JUMP` [`00bcbcd8`](#insn-00bcbcd8) → [`00bcbc6c`](#insn-00bcbc6c)
- ブロック [`00bcbcdc`](#insn-00bcbcdc) 範囲 `[['00bcbcdc', '00bcbce3']]`

## 命令位置別の参照

- [`00bcbbec`](#insn-00bcbbec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf0`](#insn-00bcbbf0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf4`](#insn-00bcbbf4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf8`](#insn-00bcbbf8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbfc`](#insn-00bcbbfc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc1c`](#insn-00bcbc1c) → [`00bcbcdc`](#insn-00bcbcdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc34`](#insn-00bcbc34) → [`00bcbc5c`](#insn-00bcbc5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc44`](#insn-00bcbc44) → [`00bcbcd4`](#insn-00bcbcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc4c`](#insn-00bcbc4c) → [`00bcbc60`](#insn-00bcbc60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc54`](#insn-00bcbc54) → `002a85ae`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbc58`](#insn-00bcbc58) → [`00b3fe98`](../00b3f/00b3fe98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b3fe98` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc64`](#insn-00bcbc64) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc80`](#insn-00bcbc80) → [`00bcbc94`](#insn-00bcbc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc90`](#insn-00bcbc90) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc9c`](#insn-00bcbc9c) → [`00bcbcbc`](#insn-00bcbcbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbca4`](#insn-00bcbca4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbca8`](#insn-00bcbca8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcac`](#insn-00bcbcac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcb0`](#insn-00bcbcb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcb8`](#insn-00bcbcb8) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcbc`](#insn-00bcbcbc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcc0`](#insn-00bcbcc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcc4`](#insn-00bcbcc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcc8`](#insn-00bcbcc8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcd8`](#insn-00bcbcd8) → [`00bcbc6c`](#insn-00bcbc6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbce0`](#insn-00bcbce0) → [`00c5a910`](../00c5a/00c5a910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a910` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbbec`](#insn-00bcbbec)

~~~json
{
  "source": "00bcbbec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf0`](#insn-00bcbbf0)

~~~json
{
  "source": "00bcbbf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf4`](#insn-00bcbbf4)

~~~json
{
  "source": "00bcbbf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf8`](#insn-00bcbbf8)

~~~json
{
  "source": "00bcbbf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbfc`](#insn-00bcbbfc)

~~~json
{
  "source": "00bcbbfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc1c`](#insn-00bcbc1c)

~~~json
{
  "source": "00bcbc1c",
  "target": "00bcbcdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc34`](#insn-00bcbc34)

~~~json
{
  "source": "00bcbc34",
  "target": "00bcbc5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc44`](#insn-00bcbc44)

~~~json
{
  "source": "00bcbc44",
  "target": "00bcbcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc4c`](#insn-00bcbc4c)

~~~json
{
  "source": "00bcbc4c",
  "target": "00bcbc60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc54`](#insn-00bcbc54)

~~~json
{
  "source": "00bcbc54",
  "target": "002a85ae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a85ae",
  "offset": 0,
  "size": 68,
  "datatype": "string",
  "bytes": "616c6c6f6361746f723c543e3a3a616c6c6f636174652873697a655f74206e29",
  "capture_start": "002a85ae",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcbc58`](#insn-00bcbc58)

~~~json
{
  "source": "00bcbc58",
  "target": "00b3fe98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc64`](#insn-00bcbc64)

~~~json
{
  "source": "00bcbc64",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc80`](#insn-00bcbc80)

~~~json
{
  "source": "00bcbc80",
  "target": "00bcbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc90`](#insn-00bcbc90)

~~~json
{
  "source": "00bcbc90",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc9c`](#insn-00bcbc9c)

~~~json
{
  "source": "00bcbc9c",
  "target": "00bcbcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbca4`](#insn-00bcbca4)

~~~json
{
  "source": "00bcbca4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbca8`](#insn-00bcbca8)

~~~json
{
  "source": "00bcbca8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcac`](#insn-00bcbcac)

~~~json
{
  "source": "00bcbcac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcb0`](#insn-00bcbcb0)

~~~json
{
  "source": "00bcbcb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcb8`](#insn-00bcbcb8)

~~~json
{
  "source": "00bcbcb8",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbcbc`](#insn-00bcbcbc)

~~~json
{
  "source": "00bcbcbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcc0`](#insn-00bcbcc0)

~~~json
{
  "source": "00bcbcc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcc4`](#insn-00bcbcc4)

~~~json
{
  "source": "00bcbcc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcc8`](#insn-00bcbcc8)

~~~json
{
  "source": "00bcbcc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcd8`](#insn-00bcbcd8)

~~~json
{
  "source": "00bcbcd8",
  "target": "00bcbc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbce0`](#insn-00bcbce0)

~~~json
{
  "source": "00bcbce0",
  "target": "00c5a910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
