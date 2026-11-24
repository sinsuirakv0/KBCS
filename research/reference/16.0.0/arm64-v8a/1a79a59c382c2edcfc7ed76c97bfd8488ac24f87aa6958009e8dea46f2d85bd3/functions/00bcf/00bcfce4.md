# 00bcfce4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b607e4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b607e4.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-753e75d7c46c857b3c5b8bcfea2a2e73)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd010c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd010c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-79e8669a456efd20685da35da3d90773)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfce4",
  "name": "_ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5e24f44ab144fea3ec9df1c6e24552babda325b57835dc3ced06181f9d676fc",
  "source_text_sha256": "f5e24f44ab144fea3ec9df1c6e24552babda325b57835dc3ced06181f9d676fc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfce4",
        "00bcfda3"
      ]
    ],
    "bytes_sha256": "2d394358d34201a5ef5aec38e4d0ffe1ed6870d8ac28c508d37f210a8817e1dc",
    "instruction_count": 48,
    "instruction_bytes": 192,
    "body_bytes": 192,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5d7b0](../00c5d/00c5d7b0.md)
- [00c5d920](../00c5d/00c5d920.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1686 bytes

~~~c

void _ZN8firebase4auth14FutureCallbackINS0_4UserEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               void *param_5)

{
  long lVar1;
  undefined4 uVar2;
  long lVar3;
  undefined8 local_78;
  undefined1 local_70;
  void *local_68;
  undefined1 auStack_60 [20];
  undefined1 local_4c;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00bcfd10 to 00ccfd2b has its CatchHandler @ 00bd0178 */
  local_4c = 0;
  uVar2 = _ZN8firebase4auth34MapFutureCallbackResultToAuthErrorEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPb
                    ();
  lVar3 = *(long *)((long)param_5 + 0x10);
                    /* try { // try from 00bcfd2c to 00ccfd7f has its CatchHandler @ 00bcfac4 */
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_60,param_5);
  local_70 = local_4c;
  local_78 = param_2;
  local_68 = param_5;
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4UserEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
            (lVar3 + 0x10,auStack_60,uVar2,param_4,&local_78);
  _ZN8firebase12FutureHandleD2Ev(auStack_60);
  _ZN8firebase12FutureHandleD2Ev(param_5);
  _ZdlPv(param_5);
                    /* try { // try from 00bcfd80 to 00ccfd8b has its CatchHandler @ 00bd0178 */
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00bcfd8c to 00ccff53 has its CatchHandler @ 00bcfac4 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcfce4"></a> `00bcfce4` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfce8"></a> `00bcfce8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfcec"></a> `00bcfcec` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfcf0"></a> `00bcfcf0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfcf4"></a> `00bcfcf4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfcf8"></a> `00bcfcf8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcfcfc"></a> `00bcfcfc` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcfd00"></a> `00bcfd00` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfd04"></a> `00bcfd04` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bcfd08"></a> `00bcfd08` | `e3 d3 00 91` | add x3,sp,#0x34 | `FALL_THROUGH`
<a id="insn-00bcfd0c"></a> `00bcfd0c` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bcfd10"></a> `00bcfd10` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcfd14"></a> `00bcfd14` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfd18"></a> `00bcfd18` | `ff d3 00 39` | strb wzr,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bcfd1c"></a> `00bcfd1c` | `01 37 02 94` | bl 0x00c5d920 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd20"></a> `00bcfd20` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfd24"></a> `00bcfd24` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bcfd28"></a> `00bcfd28` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfd2c"></a> `00bcfd2c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfd30"></a> `00bcfd30` | `17 41 00 91` | add x23,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcfd34"></a> `00bcfd34` | `33 2b 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd38"></a> `00bcfd38` | `e8 d3 40 39` | ldrb w8,[sp, #0x34] | `FALL_THROUGH`
<a id="insn-00bcfd3c"></a> `00bcfd3c` | `f5 07 00 f9` | str x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfd40"></a> `00bcfd40` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcfd44"></a> `00bcfd44` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfd48"></a> `00bcfd48` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfd4c"></a> `00bcfd4c` | `e4 23 00 91` | add x4,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfd50"></a> `00bcfd50` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcfd54"></a> `00bcfd54` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00bcfd58"></a> `00bcfd58` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bcfd5c"></a> `00bcfd5c` | `95 36 02 94` | bl 0x00c5d7b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd60"></a> `00bcfd60` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcfd64"></a> `00bcfd64` | `4b 2a 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd68"></a> `00bcfd68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfd6c"></a> `00bcfd6c` | `49 2a 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd70"></a> `00bcfd70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfd74"></a> `00bcfd74` | `4f 1f 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfd78"></a> `00bcfd78` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfd7c"></a> `00bcfd7c` | `e9 1f 40 f9` | ldr x9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bcfd80"></a> `00bcfd80` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcfd84"></a> `00bcfd84` | `e1 00 00 54` | b.ne 0x00bcfda0 | `CONDITIONAL_JUMP`
<a id="insn-00bcfd88"></a> `00bcfd88` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcfd8c"></a> `00bcfd8c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcfd90"></a> `00bcfd90` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcfd94"></a> `00bcfd94` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfd98"></a> `00bcfd98` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcfd9c"></a> `00bcfd9c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcfda0"></a> `00bcfda0` | `50 1f 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfce4`](#insn-00bcfce4) 範囲 `[['00bcfce4', '00bcfd0f']]`
  - `FALL_THROUGH` [`00bcfd0c`](#insn-00bcfd0c) → [`00bcfd10`](#insn-00bcfd10)
- ブロック [`00bcfd10`](#insn-00bcfd10) 範囲 `[['00bcfd10', '00bcfd2b']]`
  - `FALL_THROUGH` [`00bcfd28`](#insn-00bcfd28) → [`00bcfd2c`](#insn-00bcfd2c)
- ブロック [`00bcfd2c`](#insn-00bcfd2c) 範囲 `[['00bcfd2c', '00bcfd7f']]`
  - `FALL_THROUGH` [`00bcfd7c`](#insn-00bcfd7c) → [`00bcfd80`](#insn-00bcfd80)
- ブロック [`00bcfd80`](#insn-00bcfd80) 範囲 `[['00bcfd80', '00bcfd87']]`
  - `CONDITIONAL_JUMP` [`00bcfd84`](#insn-00bcfd84) → [`00bcfda0`](#insn-00bcfda0)
  - `FALL_THROUGH` [`00bcfd84`](#insn-00bcfd84) → [`00bcfd88`](#insn-00bcfd88)
- ブロック [`00bcfd88`](#insn-00bcfd88) 範囲 `[['00bcfd88', '00bcfd8b']]`
  - `FALL_THROUGH` [`00bcfd88`](#insn-00bcfd88) → [`00bcfd8c`](#insn-00bcfd8c)
- ブロック [`00bcfd8c`](#insn-00bcfd8c) 範囲 `[['00bcfd8c', '00bcfd9f']]`
- ブロック [`00bcfda0`](#insn-00bcfda0) 範囲 `[['00bcfda0', '00bcfda3']]`

## 命令位置別の参照

- [`00bcfce8`](#insn-00bcfce8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcec`](#insn-00bcfcec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcf0`](#insn-00bcfcf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcf4`](#insn-00bcfcf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd14`](#insn-00bcfd14) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd18`](#insn-00bcfd18) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd1c`](#insn-00bcfd1c) → [`00c5d920`](../00c5d/00c5d920.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d920` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd34`](#insn-00bcfd34) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd38`](#insn-00bcfd38) → `Stack[-0x4c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd3c`](#insn-00bcfd3c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd40`](#insn-00bcfd40) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd44`](#insn-00bcfd44) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd5c`](#insn-00bcfd5c) → [`00c5d7b0`](../00c5d/00c5d7b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d7b0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd64`](#insn-00bcfd64) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd6c`](#insn-00bcfd6c) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd74`](#insn-00bcfd74) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd7c`](#insn-00bcfd7c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd84`](#insn-00bcfd84) → [`00bcfda0`](#insn-00bcfda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd88`](#insn-00bcfd88) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd8c`](#insn-00bcfd8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd90`](#insn-00bcfd90) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfd94`](#insn-00bcfd94) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfda0`](#insn-00bcfda0) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfce8`](#insn-00bcfce8)

~~~json
{
  "source": "00bcfce8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcec`](#insn-00bcfcec)

~~~json
{
  "source": "00bcfcec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcf0`](#insn-00bcfcf0)

~~~json
{
  "source": "00bcfcf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcf4`](#insn-00bcfcf4)

~~~json
{
  "source": "00bcfcf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd14`](#insn-00bcfd14)

~~~json
{
  "source": "00bcfd14",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd18`](#insn-00bcfd18)

~~~json
{
  "source": "00bcfd18",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd1c`](#insn-00bcfd1c)

~~~json
{
  "source": "00bcfd1c",
  "target": "00c5d920",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd34`](#insn-00bcfd34)

~~~json
{
  "source": "00bcfd34",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd38`](#insn-00bcfd38)

~~~json
{
  "source": "00bcfd38",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd3c`](#insn-00bcfd3c)

~~~json
{
  "source": "00bcfd3c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd40`](#insn-00bcfd40)

~~~json
{
  "source": "00bcfd40",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd44`](#insn-00bcfd44)

~~~json
{
  "source": "00bcfd44",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd5c`](#insn-00bcfd5c)

~~~json
{
  "source": "00bcfd5c",
  "target": "00c5d7b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd64`](#insn-00bcfd64)

~~~json
{
  "source": "00bcfd64",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd6c`](#insn-00bcfd6c)

~~~json
{
  "source": "00bcfd6c",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd74`](#insn-00bcfd74)

~~~json
{
  "source": "00bcfd74",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfd7c`](#insn-00bcfd7c)

~~~json
{
  "source": "00bcfd7c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd84`](#insn-00bcfd84)

~~~json
{
  "source": "00bcfd84",
  "target": "00bcfda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd88`](#insn-00bcfd88)

~~~json
{
  "source": "00bcfd88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd8c`](#insn-00bcfd8c)

~~~json
{
  "source": "00bcfd8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd90`](#insn-00bcfd90)

~~~json
{
  "source": "00bcfd90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfd94`](#insn-00bcfd94)

~~~json
{
  "source": "00bcfd94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfda0`](#insn-00bcfda0)

~~~json
{
  "source": "00bcfda0",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
