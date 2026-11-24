# 00aefbb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a90784`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a90/00a90784.md) · 移動量 `+0x5f42c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-dffff552ed9d136769fce556db2308b1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aeffd8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aef/00aeffd8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-e6915e6ffe7492f8369a565a82b91541)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefbb0",
  "name": "FUN_00aefbb0",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a3f92a531927823cc78e2733d1ada6cd3d9517840b85a5542bd57d3d6db2cef",
  "source_text_sha256": "4a3f92a531927823cc78e2733d1ada6cd3d9517840b85a5542bd57d3d6db2cef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aefbb0",
        "00aefc63"
      ]
    ],
    "bytes_sha256": "228485931a4565065a2c8573a1564af2a927cbbbf8a45805d087d56ce73146a4",
    "instruction_count": 45,
    "instruction_bytes": 180,
    "body_bytes": 180,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [008b6f0c](../008b6/008b6f0c.md)
- [00b0b218](../00b0b/00b0b218.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2778 bytes

~~~c

void FUN_00aefbb0(long param_1,undefined8 *param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  ulong uVar3;
  undefined4 uVar4;
  undefined8 uVar5;
  long lVar6;
  
                    /* try { // try from 00aefbc0 to 00befbc3 has its CatchHandler @ 00aefc0c */
  iVar1 = *param_3;
  uVar5 = *param_2;
  if (iVar1 == 4) {
    lVar6 = *(long *)(param_1 + 8);
    uVar3 = FUN_008b6f0c(uVar5);
    if ((uVar3 & 1) == 0) {
      return;
    }
                    /* catch() { ... } // from try @ 00aefe00 with catch @ 00aefc4c
                       catch() { ... } // from try @ 00aeff30 with catch @ 00aefc4c
                       catch() { ... } // from try @ 00af00e4 with catch @ 00aefc4c
                       catch() { ... } // from try @ 00af0298 with catch @ 00aefc4c */
    FUN_00b0b218(lVar6 + 0x3d8,*(long *)(param_1 + 0x10),*(long *)(param_1 + 0x10) + 0x510,0);
    return;
  }
                    /* try { // try from 00aefbd4 to 00befbd7 has its CatchHandler @ 00aefc08 */
  if (iVar1 == 3) {
                    /* try { // try from 00aefbe8 to 00befbeb has its CatchHandler @ 00aefc04 */
    uVar2 = FUN_0047acb4();
    uVar3 = FUN_008b6f0c(uVar5);
                    /* try { // try from 00aefbfc to 00befbff has its CatchHandler @ 00aefc00 */
    uVar4 = 0xb;
                    /* catch() { ... } // from try @ 00aefb1c with catch @ 00aefc00
                       catch() { ... } // from try @ 00aefbfc with catch @ 00aefc00
                       try { // try from 00aefc00 to 00befc4b has its CatchHandler @ 00aef744 */
                    /* catch() { ... } // from try @ 00aefaa8 with catch @ 00aefc04
                       catch() { ... } // from try @ 00aefbe8 with catch @ 00aefc04 */
    if ((uVar3 & 1) == 0) {
      uVar4 = 0xf;
    }
  }
  else {
    if (iVar1 != 0) {
      return;
    }
    uVar2 = FUN_0047acb4();
    uVar4 = 10;
  }
                    /* catch() { ... } // from try @ 00aef9ac with catch @ 00aefc0c
                       catch() { ... } // from try @ 00aefbc0 with catch @ 00aefc0c */
                    /* catch() { ... } // from try @ 00aef92c with catch @ 00aefc10
                       catch() { ... } // from try @ 00aefbac with catch @ 00aefc10 */
                    /* catch() { ... } // from try @ 00aef8b4 with catch @ 00aefc14
                       catch() { ... } // from try @ 00aefb98 with catch @ 00aefc14 */
                    /* catch() { ... } // from try @ 00aef83c with catch @ 00aefc18
                       catch() { ... } // from try @ 00aefb84 with catch @ 00aefc18 */
                    /* catch() { ... } // from try @ 00aef7c4 with catch @ 00aefc1c
                       catch() { ... } // from try @ 00aefb70 with catch @ 00aefc1c */
  FUN_0047cd94(uVar2,uVar4,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aefbb0"></a> `00aefbb0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aefbb4"></a> `00aefbb4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefbb8"></a> `00aefbb8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefbbc"></a> `00aefbbc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aefbc0"></a> `00aefbc0` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aefbc4"></a> `00aefbc4` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aefbc8"></a> `00aefbc8` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00aefbcc"></a> `00aefbcc` | `a0 02 00 54` | b.eq 0x00aefc20 | `CONDITIONAL_JUMP`
<a id="insn-00aefbd0"></a> `00aefbd0` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aefbd4"></a> `00aefbd4` | `a0 00 00 54` | b.eq 0x00aefbe8 | `CONDITIONAL_JUMP`
<a id="insn-00aefbd8"></a> `00aefbd8` | `e8 03 00 35` | cbnz w8,0x00aefc54 | `CONDITIONAL_JUMP`
<a id="insn-00aefbdc"></a> `00aefbdc` | `36 2c e6 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00aefbe0"></a> `00aefbe0` | `41 01 80 52` | mov w1,#0xa | `FALL_THROUGH`
<a id="insn-00aefbe4"></a> `00aefbe4` | `0a 00 00 14` | b 0x00aefc0c | `UNCONDITIONAL_JUMP`
<a id="insn-00aefbe8"></a> `00aefbe8` | `33 2c e6 97` | bl 0x0047acb4 | `UNCONDITIONAL_CALL`
<a id="insn-00aefbec"></a> `00aefbec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aefbf0"></a> `00aefbf0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefbf4"></a> `00aefbf4` | `c6 1c f7 97` | bl 0x008b6f0c | `UNCONDITIONAL_CALL`
<a id="insn-00aefbf8"></a> `00aefbf8` | `e8 01 80 52` | mov w8,#0xf | `FALL_THROUGH`
<a id="insn-00aefbfc"></a> `00aefbfc` | `1f 00 00 72` | tst w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aefc00"></a> `00aefc00` | `69 01 80 52` | mov w9,#0xb | `FALL_THROUGH`
<a id="insn-00aefc04"></a> `00aefc04` | `21 11 88 1a` | csel w1,w9,w8,ne | `FALL_THROUGH`
<a id="insn-00aefc08"></a> `00aefc08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aefc0c"></a> `00aefc0c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aefc10"></a> `00aefc10` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefc14"></a> `00aefc14` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefc18"></a> `00aefc18` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aefc1c"></a> `00aefc1c` | `5e 34 e6 17` | b 0x0047cd94 | `CALL_TERMINATOR`
<a id="insn-00aefc20"></a> `00aefc20` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aefc24"></a> `00aefc24` | `14 04 40 f9` | ldr x20,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aefc28"></a> `00aefc28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aefc2c"></a> `00aefc2c` | `b8 1c f7 97` | bl 0x008b6f0c | `UNCONDITIONAL_CALL`
<a id="insn-00aefc30"></a> `00aefc30` | `20 01 00 36` | tbz w0,#0x0,0x00aefc54 | `CONDITIONAL_JUMP`
<a id="insn-00aefc34"></a> `00aefc34` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aefc38"></a> `00aefc38` | `80 62 0f 91` | add x0,x20,#0x3d8 | `FALL_THROUGH`
<a id="insn-00aefc3c"></a> `00aefc3c` | `22 40 14 91` | add x2,x1,#0x510 | `FALL_THROUGH`
<a id="insn-00aefc40"></a> `00aefc40` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aefc44"></a> `00aefc44` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefc48"></a> `00aefc48` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefc4c"></a> `00aefc4c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aefc50"></a> `00aefc50` | `72 6d 00 14` | b 0x00b0b218 | `CALL_TERMINATOR`
<a id="insn-00aefc54"></a> `00aefc54` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aefc58"></a> `00aefc58` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aefc5c"></a> `00aefc5c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aefc60"></a> `00aefc60` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aefbb0`](#insn-00aefbb0) 範囲 `[['00aefbb0', '00aefbbf']]`
  - `FALL_THROUGH` [`00aefbbc`](#insn-00aefbbc) → [`00aefbc0`](#insn-00aefbc0)
- ブロック [`00aefbc0`](#insn-00aefbc0) 範囲 `[['00aefbc0', '00aefbcf']]`
  - `CONDITIONAL_JUMP` [`00aefbcc`](#insn-00aefbcc) → [`00aefc20`](#insn-00aefc20)
  - `FALL_THROUGH` [`00aefbcc`](#insn-00aefbcc) → [`00aefbd0`](#insn-00aefbd0)
- ブロック [`00aefbd0`](#insn-00aefbd0) 範囲 `[['00aefbd0', '00aefbd3']]`
  - `FALL_THROUGH` [`00aefbd0`](#insn-00aefbd0) → [`00aefbd4`](#insn-00aefbd4)
- ブロック [`00aefbd4`](#insn-00aefbd4) 範囲 `[['00aefbd4', '00aefbd7']]`
  - `CONDITIONAL_JUMP` [`00aefbd4`](#insn-00aefbd4) → [`00aefbe8`](#insn-00aefbe8)
  - `FALL_THROUGH` [`00aefbd4`](#insn-00aefbd4) → [`00aefbd8`](#insn-00aefbd8)
- ブロック [`00aefbd8`](#insn-00aefbd8) 範囲 `[['00aefbd8', '00aefbdb']]`
  - `CONDITIONAL_JUMP` [`00aefbd8`](#insn-00aefbd8) → [`00aefc54`](#insn-00aefc54)
  - `FALL_THROUGH` [`00aefbd8`](#insn-00aefbd8) → [`00aefbdc`](#insn-00aefbdc)
- ブロック [`00aefbdc`](#insn-00aefbdc) 範囲 `[['00aefbdc', '00aefbe7']]`
  - `UNCONDITIONAL_JUMP` [`00aefbe4`](#insn-00aefbe4) → [`00aefc0c`](#insn-00aefc0c)
- ブロック [`00aefbe8`](#insn-00aefbe8) 範囲 `[['00aefbe8', '00aefbfb']]`
  - `FALL_THROUGH` [`00aefbf8`](#insn-00aefbf8) → [`00aefbfc`](#insn-00aefbfc)
- ブロック [`00aefbfc`](#insn-00aefbfc) 範囲 `[['00aefbfc', '00aefbff']]`
  - `FALL_THROUGH` [`00aefbfc`](#insn-00aefbfc) → [`00aefc00`](#insn-00aefc00)
- ブロック [`00aefc00`](#insn-00aefc00) 範囲 `[['00aefc00', '00aefc03']]`
  - `FALL_THROUGH` [`00aefc00`](#insn-00aefc00) → [`00aefc04`](#insn-00aefc04)
- ブロック [`00aefc04`](#insn-00aefc04) 範囲 `[['00aefc04', '00aefc07']]`
  - `FALL_THROUGH` [`00aefc04`](#insn-00aefc04) → [`00aefc08`](#insn-00aefc08)
- ブロック [`00aefc08`](#insn-00aefc08) 範囲 `[['00aefc08', '00aefc0b']]`
  - `FALL_THROUGH` [`00aefc08`](#insn-00aefc08) → [`00aefc0c`](#insn-00aefc0c)
- ブロック [`00aefc0c`](#insn-00aefc0c) 範囲 `[['00aefc0c', '00aefc0f']]`
  - `FALL_THROUGH` [`00aefc0c`](#insn-00aefc0c) → [`00aefc10`](#insn-00aefc10)
- ブロック [`00aefc10`](#insn-00aefc10) 範囲 `[['00aefc10', '00aefc13']]`
  - `FALL_THROUGH` [`00aefc10`](#insn-00aefc10) → [`00aefc14`](#insn-00aefc14)
- ブロック [`00aefc14`](#insn-00aefc14) 範囲 `[['00aefc14', '00aefc17']]`
  - `FALL_THROUGH` [`00aefc14`](#insn-00aefc14) → [`00aefc18`](#insn-00aefc18)
- ブロック [`00aefc18`](#insn-00aefc18) 範囲 `[['00aefc18', '00aefc1b']]`
  - `FALL_THROUGH` [`00aefc18`](#insn-00aefc18) → [`00aefc1c`](#insn-00aefc1c)
- ブロック [`00aefc1c`](#insn-00aefc1c) 範囲 `[['00aefc1c', '00aefc1f']]`
- ブロック [`00aefc20`](#insn-00aefc20) 範囲 `[['00aefc20', '00aefc33']]`
  - `CONDITIONAL_JUMP` [`00aefc30`](#insn-00aefc30) → [`00aefc54`](#insn-00aefc54)
  - `FALL_THROUGH` [`00aefc30`](#insn-00aefc30) → [`00aefc34`](#insn-00aefc34)
- ブロック [`00aefc34`](#insn-00aefc34) 範囲 `[['00aefc34', '00aefc4b']]`
  - `FALL_THROUGH` [`00aefc48`](#insn-00aefc48) → [`00aefc4c`](#insn-00aefc4c)
- ブロック [`00aefc4c`](#insn-00aefc4c) 範囲 `[['00aefc4c', '00aefc53']]`
- ブロック [`00aefc54`](#insn-00aefc54) 範囲 `[['00aefc54', '00aefc63']]`

## 命令位置別の参照

- [`00aefbb0`](#insn-00aefbb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbb4`](#insn-00aefbb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbb8`](#insn-00aefbb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbcc`](#insn-00aefbcc) → [`00aefc20`](#insn-00aefc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbd4`](#insn-00aefbd4) → [`00aefbe8`](#insn-00aefbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbd8`](#insn-00aefbd8) → [`00aefc54`](#insn-00aefc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbdc`](#insn-00aefbdc) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00aefbe4`](#insn-00aefbe4) → [`00aefc0c`](#insn-00aefc0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefbe8`](#insn-00aefbe8) → [`0047acb4`](../0047a/0047acb4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acb4` · 推定シンボル `None` · 推定型 `None`
- [`00aefbf4`](#insn-00aefbf4) → [`008b6f0c`](../008b6/008b6f0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f0c` · 推定シンボル `None` · 推定型 `None`
- [`00aefc10`](#insn-00aefc10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc14`](#insn-00aefc14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc18`](#insn-00aefc18) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc1c`](#insn-00aefc1c) → [`0047cd94`](../0047c/0047cd94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047cd94` · 推定シンボル `None` · 推定型 `None`
- [`00aefc2c`](#insn-00aefc2c) → [`008b6f0c`](../008b6/008b6f0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6f0c` · 推定シンボル `None` · 推定型 `None`
- [`00aefc30`](#insn-00aefc30) → [`00aefc54`](#insn-00aefc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc44`](#insn-00aefc44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc48`](#insn-00aefc48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc4c`](#insn-00aefc4c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc50`](#insn-00aefc50) → [`00b0b218`](../00b0b/00b0b218.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0b218` · 推定シンボル `None` · 推定型 `None`
- [`00aefc54`](#insn-00aefc54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc58`](#insn-00aefc58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aefc5c`](#insn-00aefc5c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aefbb0`](#insn-00aefbb0)

~~~json
{
  "source": "00aefbb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbb4`](#insn-00aefbb4)

~~~json
{
  "source": "00aefbb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbb8`](#insn-00aefbb8)

~~~json
{
  "source": "00aefbb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbcc`](#insn-00aefbcc)

~~~json
{
  "source": "00aefbcc",
  "target": "00aefc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbd4`](#insn-00aefbd4)

~~~json
{
  "source": "00aefbd4",
  "target": "00aefbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbd8`](#insn-00aefbd8)

~~~json
{
  "source": "00aefbd8",
  "target": "00aefc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbdc`](#insn-00aefbdc)

~~~json
{
  "source": "00aefbdc",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefbe4`](#insn-00aefbe4)

~~~json
{
  "source": "00aefbe4",
  "target": "00aefc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefbe8`](#insn-00aefbe8)

~~~json
{
  "source": "00aefbe8",
  "target": "0047acb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefbf4`](#insn-00aefbf4)

~~~json
{
  "source": "00aefbf4",
  "target": "008b6f0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc10`](#insn-00aefc10)

~~~json
{
  "source": "00aefc10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc14`](#insn-00aefc14)

~~~json
{
  "source": "00aefc14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc18`](#insn-00aefc18)

~~~json
{
  "source": "00aefc18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc1c`](#insn-00aefc1c)

~~~json
{
  "source": "00aefc1c",
  "target": "0047cd94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc2c`](#insn-00aefc2c)

~~~json
{
  "source": "00aefc2c",
  "target": "008b6f0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc30`](#insn-00aefc30)

~~~json
{
  "source": "00aefc30",
  "target": "00aefc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc44`](#insn-00aefc44)

~~~json
{
  "source": "00aefc44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc48`](#insn-00aefc48)

~~~json
{
  "source": "00aefc48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc4c`](#insn-00aefc4c)

~~~json
{
  "source": "00aefc4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc50`](#insn-00aefc50)

~~~json
{
  "source": "00aefc50",
  "target": "00b0b218",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aefc54`](#insn-00aefc54)

~~~json
{
  "source": "00aefc54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc58`](#insn-00aefc58)

~~~json
{
  "source": "00aefc58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aefc5c`](#insn-00aefc5c)

~~~json
{
  "source": "00aefc5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
