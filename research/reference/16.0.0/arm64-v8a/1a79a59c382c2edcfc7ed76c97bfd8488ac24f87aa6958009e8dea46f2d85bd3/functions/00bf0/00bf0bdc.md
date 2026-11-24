# 00bf0bdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b74194`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b74/00b74194.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0018.md#compare-36e880165397fc0409685d84684bacd7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf1004`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1004.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-090cb8ad53f1bdb69ff3d9e5490878c0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf0bdc",
  "name": "FUN_00bf0bdc",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9e2bc01d9c5124797aebb75c51676b5b72926918da20f3a041a0a40123b90cc1",
  "source_text_sha256": "9e2bc01d9c5124797aebb75c51676b5b72926918da20f3a041a0a40123b90cc1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf0bdc",
        "00bf0d0f"
      ]
    ],
    "bytes_sha256": "d148c23dbd4316563f54ce5bfb9e5a9026ec4c5c229c658e288b42a53021916d",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bf0ea4](../00bf0/00bf0ea4.md)

## 呼び出し先

- [0043b724](../0043b/0043b724.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57b40](../00c57/00c57b40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1326 bytes

~~~c

void FUN_00bf0bdc(ulong *param_1,ulong param_2,ulong param_3,long param_4,size_t param_5,
                 long param_6,long param_7)

{
  ulong uVar1;
  size_t __n;
  void *__dest;
  byte *__src;
  ulong uVar2;
  
  if (param_3 <= -param_2 - 9) {
    __src = (byte *)param_1[2];
    if ((*param_1 & 1) == 0) {
      __src = (byte *)((long)param_1 + 1);
    }
    if (param_2 < 0x7ffffffffffffff3) {
      uVar1 = param_3 + param_2;
      if (param_3 + param_2 <= param_2 * 2) {
        uVar1 = param_2 * 2;
      }
      if (uVar1 < 0x17) {
        uVar2 = 0x17;
      }
      else {
        uVar2 = (uVar1 & 0xfffffffffffffff8) + 8;
        if ((uVar1 | 7) != 0x17) {
          uVar2 = uVar1 | 7;
        }
        uVar2 = uVar2 + 1;
      }
    }
    else {
      uVar2 = 0xfffffffffffffff7;
    }
    __dest = (void *)_Znwm(uVar2);
    if (param_5 != 0) {
      memmove(__dest,__src,param_5);
    }
    __n = param_4 - (param_6 + param_5);
    if (__n != 0) {
      memmove((void *)((long)__dest + param_7 + param_5),__src + param_6 + param_5,__n);
    }
    if (param_2 != 0x16) {
      _ZdlPv(__src);
    }
    *param_1 = uVar2 | 1;
    param_1[1] = (param_4 - param_6) + param_7;
    param_1[2] = (ulong)__dest;
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_0043b724(param_1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf0bdc"></a> `00bf0bdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf0be0"></a> `00bf0be0` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00bf0be4"></a> `00bf0be4` | `fb 0b 00 f9` | str x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0be8"></a> `00bf0be8` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf0bec"></a> `00bf0bec` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf0bf0"></a> `00bf0bf0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf0bf4"></a> `00bf0bf4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf0bf8"></a> `00bf0bf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf0bfc"></a> `00bf0bfc` | `08 01 80 92` | mov x8,#-0x9 | `FALL_THROUGH`
<a id="insn-00bf0c00"></a> `00bf0c00` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bf0c04"></a> `00bf0c04` | `08 01 01 cb` | sub x8,x8,x1 | `FALL_THROUGH`
<a id="insn-00bf0c08"></a> `00bf0c08` | `1f 01 02 eb` | cmp x8,x2 | `FALL_THROUGH`
<a id="insn-00bf0c0c"></a> `00bf0c0c` | `e3 07 00 54` | b.cc 0x00bf0d08 | `CONDITIONAL_JUMP`
<a id="insn-00bf0c10"></a> `00bf0c10` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00bf0c14"></a> `00bf0c14` | `c9 0a 40 f9` | ldr x9,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0c18"></a> `00bf0c18` | `f3 03 06 aa` | mov x19,x6 | `FALL_THROUGH`
<a id="insn-00bf0c1c"></a> `00bf0c1c` | `f4 03 05 aa` | mov x20,x5 | `FALL_THROUGH`
<a id="insn-00bf0c20"></a> `00bf0c20` | `f8 03 04 aa` | mov x24,x4 | `FALL_THROUGH`
<a id="insn-00bf0c24"></a> `00bf0c24` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bf0c28"></a> `00bf0c28` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf0c2c"></a> `00bf0c2c` | `a8 01 80 92` | mov x8,#-0xe | `FALL_THROUGH`
<a id="insn-00bf0c30"></a> `00bf0c30` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bf0c34"></a> `00bf0c34` | `e8 ff ef f2` | movk x8,#0x7fff, LSL #48 | `FALL_THROUGH`
<a id="insn-00bf0c38"></a> `00bf0c38` | `39 15 96 9a` | csinc x25,x9,x22,ne | `FALL_THROUGH`
<a id="insn-00bf0c3c"></a> `00bf0c3c` | `3f 00 08 eb` | cmp x1,x8 | `FALL_THROUGH`
<a id="insn-00bf0c40"></a> `00bf0c40` | `28 01 00 54` | b.hi 0x00bf0c64 | `CONDITIONAL_JUMP`
<a id="insn-00bf0c44"></a> `00bf0c44` | `e8 fa 7f d3` | lsl x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bf0c48"></a> `00bf0c48` | `49 00 17 8b` | add x9,x2,x23 | `FALL_THROUGH`
<a id="insn-00bf0c4c"></a> `00bf0c4c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bf0c50"></a> `00bf0c50` | `28 81 88 9a` | csel x8,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bf0c54"></a> `00bf0c54` | `1f 5d 00 f1` | cmp x8,#0x17 | `FALL_THROUGH`
<a id="insn-00bf0c58"></a> `00bf0c58` | `a2 00 00 54` | b.cs 0x00bf0c6c | `CONDITIONAL_JUMP`
<a id="insn-00bf0c5c"></a> `00bf0c5c` | `fa 02 80 52` | mov w26,#0x17 | `FALL_THROUGH`
<a id="insn-00bf0c60"></a> `00bf0c60` | `09 00 00 14` | b 0x00bf0c84 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0c64"></a> `00bf0c64` | `1a 01 80 92` | mov x26,#-0x9 | `FALL_THROUGH`
<a id="insn-00bf0c68"></a> `00bf0c68` | `07 00 00 14` | b 0x00bf0c84 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf0c6c"></a> `00bf0c6c` | `09 f1 7d 92` | and x9,x8,#-0x8 | `FALL_THROUGH`
<a id="insn-00bf0c70"></a> `00bf0c70` | `08 09 40 b2` | orr x8,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00bf0c74"></a> `00bf0c74` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bf0c78"></a> `00bf0c78` | `1f 5d 00 f1` | cmp x8,#0x17 | `FALL_THROUGH`
<a id="insn-00bf0c7c"></a> `00bf0c7c` | `28 01 88 9a` | csel x8,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bf0c80"></a> `00bf0c80` | `1a 05 00 91` | add x26,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf0c84"></a> `00bf0c84` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bf0c88"></a> `00bf0c88` | `82 9b 01 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0c8c"></a> `00bf0c8c` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00bf0c90"></a> `00bf0c90` | `b8 00 00 b4` | cbz x24,0x00bf0ca4 | `CONDITIONAL_JUMP`
<a id="insn-00bf0c94"></a> `00bf0c94` | `e0 03 1b aa` | mov x0,x27 | `FALL_THROUGH`
<a id="insn-00bf0c98"></a> `00bf0c98` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bf0c9c"></a> `00bf0c9c` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bf0ca0"></a> `00bf0ca0` | `a8 9b 01 94` | bl 0x00c57b40 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0ca4"></a> `00bf0ca4` | `88 02 18 8b` | add x8,x20,x24 | `FALL_THROUGH`
<a id="insn-00bf0ca8"></a> `00bf0ca8` | `a2 02 08 eb` | subs x2,x21,x8 | `FALL_THROUGH`
<a id="insn-00bf0cac"></a> `00bf0cac` | `c0 00 00 54` | b.eq 0x00bf0cc4 | `CONDITIONAL_JUMP`
<a id="insn-00bf0cb0"></a> `00bf0cb0` | `28 03 18 8b` | add x8,x25,x24 | `FALL_THROUGH`
<a id="insn-00bf0cb4"></a> `00bf0cb4` | `69 03 18 8b` | add x9,x27,x24 | `FALL_THROUGH`
<a id="insn-00bf0cb8"></a> `00bf0cb8` | `20 01 13 8b` | add x0,x9,x19 | `FALL_THROUGH`
<a id="insn-00bf0cbc"></a> `00bf0cbc` | `01 01 14 8b` | add x1,x8,x20 | `FALL_THROUGH`
<a id="insn-00bf0cc0"></a> `00bf0cc0` | `a0 9b 01 94` | bl 0x00c57b40 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0cc4"></a> `00bf0cc4` | `ff 5a 00 f1` | cmp x23,#0x16 | `FALL_THROUGH`
<a id="insn-00bf0cc8"></a> `00bf0cc8` | `60 00 00 54` | b.eq 0x00bf0cd4 | `CONDITIONAL_JUMP`
<a id="insn-00bf0ccc"></a> `00bf0ccc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bf0cd0"></a> `00bf0cd0` | `78 9b 01 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf0cd4"></a> `00bf0cd4` | `a9 02 14 cb` | sub x9,x21,x20 | `FALL_THROUGH`
<a id="insn-00bf0cd8"></a> `00bf0cd8` | `48 03 40 b2` | orr x8,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00bf0cdc"></a> `00bf0cdc` | `29 01 13 8b` | add x9,x9,x19 | `FALL_THROUGH`
<a id="insn-00bf0ce0"></a> `00bf0ce0` | `c8 02 00 f9` | str x8,[x22] | `FALL_THROUGH`
<a id="insn-00bf0ce4"></a> `00bf0ce4` | `c9 ee 00 a9` | stp x9,x27,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bf0ce8"></a> `00bf0ce8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf0cec"></a> `00bf0cec` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf0cf0"></a> `00bf0cf0` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf0cf4"></a> `00bf0cf4` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf0cf8"></a> `00bf0cf8` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf0cfc"></a> `00bf0cfc` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00bf0d00"></a> `00bf0d00` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf0d04"></a> `00bf0d04` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf0d08"></a> `00bf0d08` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bf0d0c"></a> `00bf0d0c` | `86 2a e1 97` | bl 0x0043b724 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf0bdc`](#insn-00bf0bdc) 範囲 `[['00bf0bdc', '00bf0c0f']]`
  - `CONDITIONAL_JUMP` [`00bf0c0c`](#insn-00bf0c0c) → [`00bf0d08`](#insn-00bf0d08)
  - `FALL_THROUGH` [`00bf0c0c`](#insn-00bf0c0c) → [`00bf0c10`](#insn-00bf0c10)
- ブロック [`00bf0c10`](#insn-00bf0c10) 範囲 `[['00bf0c10', '00bf0c43']]`
  - `CONDITIONAL_JUMP` [`00bf0c40`](#insn-00bf0c40) → [`00bf0c64`](#insn-00bf0c64)
  - `FALL_THROUGH` [`00bf0c40`](#insn-00bf0c40) → [`00bf0c44`](#insn-00bf0c44)
- ブロック [`00bf0c44`](#insn-00bf0c44) 範囲 `[['00bf0c44', '00bf0c5b']]`
  - `CONDITIONAL_JUMP` [`00bf0c58`](#insn-00bf0c58) → [`00bf0c6c`](#insn-00bf0c6c)
  - `FALL_THROUGH` [`00bf0c58`](#insn-00bf0c58) → [`00bf0c5c`](#insn-00bf0c5c)
- ブロック [`00bf0c5c`](#insn-00bf0c5c) 範囲 `[['00bf0c5c', '00bf0c63']]`
  - `UNCONDITIONAL_JUMP` [`00bf0c60`](#insn-00bf0c60) → [`00bf0c84`](#insn-00bf0c84)
- ブロック [`00bf0c64`](#insn-00bf0c64) 範囲 `[['00bf0c64', '00bf0c6b']]`
  - `UNCONDITIONAL_JUMP` [`00bf0c68`](#insn-00bf0c68) → [`00bf0c84`](#insn-00bf0c84)
- ブロック [`00bf0c6c`](#insn-00bf0c6c) 範囲 `[['00bf0c6c', '00bf0c83']]`
  - `FALL_THROUGH` [`00bf0c80`](#insn-00bf0c80) → [`00bf0c84`](#insn-00bf0c84)
- ブロック [`00bf0c84`](#insn-00bf0c84) 範囲 `[['00bf0c84', '00bf0c93']]`
  - `CONDITIONAL_JUMP` [`00bf0c90`](#insn-00bf0c90) → [`00bf0ca4`](#insn-00bf0ca4)
  - `FALL_THROUGH` [`00bf0c90`](#insn-00bf0c90) → [`00bf0c94`](#insn-00bf0c94)
- ブロック [`00bf0c94`](#insn-00bf0c94) 範囲 `[['00bf0c94', '00bf0ca3']]`
  - `FALL_THROUGH` [`00bf0ca0`](#insn-00bf0ca0) → [`00bf0ca4`](#insn-00bf0ca4)
- ブロック [`00bf0ca4`](#insn-00bf0ca4) 範囲 `[['00bf0ca4', '00bf0caf']]`
  - `CONDITIONAL_JUMP` [`00bf0cac`](#insn-00bf0cac) → [`00bf0cc4`](#insn-00bf0cc4)
  - `FALL_THROUGH` [`00bf0cac`](#insn-00bf0cac) → [`00bf0cb0`](#insn-00bf0cb0)
- ブロック [`00bf0cb0`](#insn-00bf0cb0) 範囲 `[['00bf0cb0', '00bf0cc3']]`
  - `FALL_THROUGH` [`00bf0cc0`](#insn-00bf0cc0) → [`00bf0cc4`](#insn-00bf0cc4)
- ブロック [`00bf0cc4`](#insn-00bf0cc4) 範囲 `[['00bf0cc4', '00bf0ccb']]`
  - `CONDITIONAL_JUMP` [`00bf0cc8`](#insn-00bf0cc8) → [`00bf0cd4`](#insn-00bf0cd4)
  - `FALL_THROUGH` [`00bf0cc8`](#insn-00bf0cc8) → [`00bf0ccc`](#insn-00bf0ccc)
- ブロック [`00bf0ccc`](#insn-00bf0ccc) 範囲 `[['00bf0ccc', '00bf0cd3']]`
  - `FALL_THROUGH` [`00bf0cd0`](#insn-00bf0cd0) → [`00bf0cd4`](#insn-00bf0cd4)
- ブロック [`00bf0cd4`](#insn-00bf0cd4) 範囲 `[['00bf0cd4', '00bf0d07']]`
- ブロック [`00bf0d08`](#insn-00bf0d08) 範囲 `[['00bf0d08', '00bf0d0f']]`

## 命令位置別の参照

- [`00bf0be0`](#insn-00bf0be0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0be4`](#insn-00bf0be4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0be8`](#insn-00bf0be8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0bec`](#insn-00bf0bec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0bf0`](#insn-00bf0bf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0bf4`](#insn-00bf0bf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0c0c`](#insn-00bf0c0c) → [`00bf0d08`](#insn-00bf0d08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0c40`](#insn-00bf0c40) → [`00bf0c64`](#insn-00bf0c64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0c58`](#insn-00bf0c58) → [`00bf0c6c`](#insn-00bf0c6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0c60`](#insn-00bf0c60) → [`00bf0c84`](#insn-00bf0c84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0c68`](#insn-00bf0c68) → [`00bf0c84`](#insn-00bf0c84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0c88`](#insn-00bf0c88) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bf0c90`](#insn-00bf0c90) → [`00bf0ca4`](#insn-00bf0ca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0ca0`](#insn-00bf0ca0) → [`00c57b40`](../00c57/00c57b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b40` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cac`](#insn-00bf0cac) → [`00bf0cc4`](#insn-00bf0cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cc0`](#insn-00bf0cc0) → [`00c57b40`](../00c57/00c57b40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b40` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cc8`](#insn-00bf0cc8) → [`00bf0cd4`](#insn-00bf0cd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cd0`](#insn-00bf0cd0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bf0ce8`](#insn-00bf0ce8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cec`](#insn-00bf0cec) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cf0`](#insn-00bf0cf0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cf4`](#insn-00bf0cf4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cf8`](#insn-00bf0cf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0cfc`](#insn-00bf0cfc) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf0d0c`](#insn-00bf0d0c) → [`0043b724`](../0043b/0043b724.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b724` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf0be0`](#insn-00bf0be0)

~~~json
{
  "source": "00bf0be0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0be4`](#insn-00bf0be4)

~~~json
{
  "source": "00bf0be4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0be8`](#insn-00bf0be8)

~~~json
{
  "source": "00bf0be8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0bec`](#insn-00bf0bec)

~~~json
{
  "source": "00bf0bec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0bf0`](#insn-00bf0bf0)

~~~json
{
  "source": "00bf0bf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0bf4`](#insn-00bf0bf4)

~~~json
{
  "source": "00bf0bf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0c0c`](#insn-00bf0c0c)

~~~json
{
  "source": "00bf0c0c",
  "target": "00bf0d08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0c40`](#insn-00bf0c40)

~~~json
{
  "source": "00bf0c40",
  "target": "00bf0c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0c58`](#insn-00bf0c58)

~~~json
{
  "source": "00bf0c58",
  "target": "00bf0c6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0c60`](#insn-00bf0c60)

~~~json
{
  "source": "00bf0c60",
  "target": "00bf0c84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0c68`](#insn-00bf0c68)

~~~json
{
  "source": "00bf0c68",
  "target": "00bf0c84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0c88`](#insn-00bf0c88)

~~~json
{
  "source": "00bf0c88",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0c90`](#insn-00bf0c90)

~~~json
{
  "source": "00bf0c90",
  "target": "00bf0ca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0ca0`](#insn-00bf0ca0)

~~~json
{
  "source": "00bf0ca0",
  "target": "00c57b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0cac`](#insn-00bf0cac)

~~~json
{
  "source": "00bf0cac",
  "target": "00bf0cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0cc0`](#insn-00bf0cc0)

~~~json
{
  "source": "00bf0cc0",
  "target": "00c57b40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0cc8`](#insn-00bf0cc8)

~~~json
{
  "source": "00bf0cc8",
  "target": "00bf0cd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0cd0`](#insn-00bf0cd0)

~~~json
{
  "source": "00bf0cd0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf0ce8`](#insn-00bf0ce8)

~~~json
{
  "source": "00bf0ce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0cec`](#insn-00bf0cec)

~~~json
{
  "source": "00bf0cec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0cf0`](#insn-00bf0cf0)

~~~json
{
  "source": "00bf0cf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0cf4`](#insn-00bf0cf4)

~~~json
{
  "source": "00bf0cf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0cf8`](#insn-00bf0cf8)

~~~json
{
  "source": "00bf0cf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0cfc`](#insn-00bf0cfc)

~~~json
{
  "source": "00bf0cfc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf0d0c`](#insn-00bf0d0c)

~~~json
{
  "source": "00bf0d0c",
  "target": "0043b724",
  "target_space": "ram",
  "resolution": "function"
}
~~~
