# 00bdf1bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6fcbc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6f/00b6fcbc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0071.md#compare-3bd111fffbc00e18c1c1ccd1708ce38c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdf5e4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdf/00bdf5e4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-4675b770192548ab460b8987fa4b1a79)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf1bc",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0af8bd715f05e1e924b28bf44ae6c532f2a9193f09925df1531d1f879c632e93",
  "source_text_sha256": "0af8bd715f05e1e924b28bf44ae6c532f2a9193f09925df1531d1f879c632e93",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdf1bc",
        "00bdf23f"
      ]
    ],
    "bytes_sha256": "0a6c82355a5c88f5aff7510df476f2ab9b510875c7b856bd7c9711449acd46b8",
    "instruction_count": 33,
    "instruction_bytes": 132,
    "body_bytes": 132,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5af90](../00c5a/00c5af90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 651 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo11provider_idEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_004977f4(uVar2,lVar1,DAT_011269c8);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdf1bc"></a> `00bdf1bc` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bdf1c0"></a> `00bdf1c0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf1c4"></a> `00bdf1c4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf1c8"></a> `00bdf1c8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bdf1cc"></a> `00bdf1cc` | `09 d4 49 a9` | ldp x9,x21,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf1d0"></a> `00bdf1d0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdf1d4"></a> `00bdf1d4` | `20 01 40 f9` | ldr x0,[x9] | `FALL_THROUGH`
<a id="insn-00bdf1d8"></a> `00bdf1d8` | `aa ee 01 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf1dc"></a> `00bdf1dc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdf1e0"></a> `00bdf1e0` | `f5 00 00 b4` | cbz x21,0x00bdf1fc | `CONDITIONAL_JUMP`
<a id="insn-00bdf1e4"></a> `00bdf1e4` | `28 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdf1e8"></a> `00bdf1e8` | `02 e5 44 f9` | ldr x2,[x8, #0x9c8] | `FALL_THROUGH`
<a id="insn-00bdf1ec"></a> `00bdf1ec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf1f0"></a> `00bdf1f0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf1f4"></a> `00bdf1f4` | `80 e1 e2 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf1f8"></a> `00bdf1f8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdf1fc"></a> `00bdf1fc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf200"></a> `00bdf200` | `58 ee 01 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdf204"></a> `00bdf204` | `35 01 00 b4` | cbz x21,0x00bdf228 | `CONDITIONAL_JUMP`
<a id="insn-00bdf208"></a> `00bdf208` | `00 01 00 37` | tbnz w0,#0x0,0x00bdf228 | `CONDITIONAL_JUMP`
<a id="insn-00bdf20c"></a> `00bdf20c` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bdf210"></a> `00bdf210` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdf214"></a> `00bdf214` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf218"></a> `00bdf218` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf21c"></a> `00bdf21c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdf220"></a> `00bdf220` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf224"></a> `00bdf224` | `5b ef 01 14` | b 0x00c5af90 | `CALL_TERMINATOR`
<a id="insn-00bdf228"></a> `00bdf228` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bdf22c"></a> `00bdf22c` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf230"></a> `00bdf230` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdf234"></a> `00bdf234` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdf238"></a> `00bdf238` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bdf23c"></a> `00bdf23c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdf1bc`](#insn-00bdf1bc) 範囲 `[['00bdf1bc', '00bdf1e3']]`
  - `CONDITIONAL_JUMP` [`00bdf1e0`](#insn-00bdf1e0) → [`00bdf1fc`](#insn-00bdf1fc)
  - `FALL_THROUGH` [`00bdf1e0`](#insn-00bdf1e0) → [`00bdf1e4`](#insn-00bdf1e4)
- ブロック [`00bdf1e4`](#insn-00bdf1e4) 範囲 `[['00bdf1e4', '00bdf1fb']]`
  - `FALL_THROUGH` [`00bdf1f8`](#insn-00bdf1f8) → [`00bdf1fc`](#insn-00bdf1fc)
- ブロック [`00bdf1fc`](#insn-00bdf1fc) 範囲 `[['00bdf1fc', '00bdf207']]`
  - `CONDITIONAL_JUMP` [`00bdf204`](#insn-00bdf204) → [`00bdf228`](#insn-00bdf228)
  - `FALL_THROUGH` [`00bdf204`](#insn-00bdf204) → [`00bdf208`](#insn-00bdf208)
- ブロック [`00bdf208`](#insn-00bdf208) 範囲 `[['00bdf208', '00bdf20b']]`
  - `CONDITIONAL_JUMP` [`00bdf208`](#insn-00bdf208) → [`00bdf228`](#insn-00bdf228)
  - `FALL_THROUGH` [`00bdf208`](#insn-00bdf208) → [`00bdf20c`](#insn-00bdf20c)
- ブロック [`00bdf20c`](#insn-00bdf20c) 範囲 `[['00bdf20c', '00bdf227']]`
- ブロック [`00bdf228`](#insn-00bdf228) 範囲 `[['00bdf228', '00bdf23f']]`

## 命令位置別の参照

- [`00bdf1bc`](#insn-00bdf1bc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf1c0`](#insn-00bdf1c0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf1c4`](#insn-00bdf1c4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf1d8`](#insn-00bdf1d8) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bdf1e0`](#insn-00bdf1e0) → [`00bdf1fc`](#insn-00bdf1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf1e8`](#insn-00bdf1e8) → `011269c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdf1f4`](#insn-00bdf1f4) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bdf200`](#insn-00bdf200) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bdf204`](#insn-00bdf204) → [`00bdf228`](#insn-00bdf228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf208`](#insn-00bdf208) → [`00bdf228`](#insn-00bdf228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf214`](#insn-00bdf214) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf218`](#insn-00bdf218) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf224`](#insn-00bdf224) → [`00c5af90`](../00c5a/00c5af90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af90` · 推定シンボル `None` · 推定型 `None`
- [`00bdf230`](#insn-00bdf230) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdf234`](#insn-00bdf234) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdf1bc`](#insn-00bdf1bc)

~~~json
{
  "source": "00bdf1bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf1c0`](#insn-00bdf1c0)

~~~json
{
  "source": "00bdf1c0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf1c4`](#insn-00bdf1c4)

~~~json
{
  "source": "00bdf1c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf1d8`](#insn-00bdf1d8)

~~~json
{
  "source": "00bdf1d8",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf1e0`](#insn-00bdf1e0)

~~~json
{
  "source": "00bdf1e0",
  "target": "00bdf1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf1e8`](#insn-00bdf1e8)

~~~json
{
  "source": "00bdf1e8",
  "target": "011269c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011269c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdf1f4`](#insn-00bdf1f4)

~~~json
{
  "source": "00bdf1f4",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf200`](#insn-00bdf200)

~~~json
{
  "source": "00bdf200",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf204`](#insn-00bdf204)

~~~json
{
  "source": "00bdf204",
  "target": "00bdf228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf208`](#insn-00bdf208)

~~~json
{
  "source": "00bdf208",
  "target": "00bdf228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf214`](#insn-00bdf214)

~~~json
{
  "source": "00bdf214",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf218`](#insn-00bdf218)

~~~json
{
  "source": "00bdf218",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf224`](#insn-00bdf224)

~~~json
{
  "source": "00bdf224",
  "target": "00c5af90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdf230`](#insn-00bdf230)

~~~json
{
  "source": "00bdf230",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdf234`](#insn-00bdf234)

~~~json
{
  "source": "00bdf234",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
