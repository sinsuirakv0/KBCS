# 00bceff0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5faf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5faf0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0004.md#compare-1239ed369c78fee28a0eb44aa08b8796)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcf418`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcf418.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-292dd17e7999051b74d54ef18be09347)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceff0",
  "name": "_ZN8firebase4auth4Auth7SignOutEv",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df63bb06c0cce2caf2c8595bf4e4173c06290723b8d1dc90a4b3c3630b0cc19d",
  "source_text_sha256": "df63bb06c0cce2caf2c8595bf4e4173c06290723b8d1dc90a4b3c3630b0cc19d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bceff0",
        "00bcf06b"
      ]
    ],
    "bytes_sha256": "0775801f02c9ff6567cea032d3a2f025fcca9149c637f94516c35c56dcb13116",
    "instruction_count": 31,
    "instruction_bytes": 124,
    "body_bytes": 124,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5a620](../00c5a/00c5a620.md)

## 呼び出し先

- [00574cac](../00574/00574cac.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d880](../00c5d/00c5d880.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 512 bytes

~~~c

void _ZN8firebase4auth4Auth7SignOutEv(long *param_1)

{
  undefined8 uVar1;
  long lVar2;
  
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
  FUN_00574cac(uVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_01126380);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  lVar2 = *param_1;
  _ZN8firebase5Mutex7AcquireEv(lVar2 + 0x18);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,*param_1 + 0x200);
  _ZN8firebase5Mutex7ReleaseEv(lVar2 + 0x18);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bceff0"></a> `00bceff0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bceff4"></a> `00bceff4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bceff8"></a> `00bceff8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bceffc"></a> `00bceffc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf000"></a> `00bcf000` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcf004"></a> `00bcf004` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcf008"></a> `00bcf008` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcf00c"></a> `00bcf00c` | `1d 2f 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf010"></a> `00bcf010` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcf014"></a> `00bcf014` | `a9 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcf018"></a> `00bcf018` | `22 c1 41 f9` | ldr x2,[x9, #0x380] | `FALL_THROUGH`
<a id="insn-00bcf01c"></a> `00bcf01c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcf020"></a> `00bcf020` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcf024"></a> `00bcf024` | `22 97 e6 97` | bl 0x00574cac | `UNCONDITIONAL_CALL`
<a id="insn-00bcf028"></a> `00bcf028` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcf02c"></a> `00bcf02c` | `cd 2e 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf030"></a> `00bcf030` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcf034"></a> `00bcf034` | `13 61 00 91` | add x19,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bcf038"></a> `00bcf038` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf03c"></a> `00bcf03c` | `71 2d 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf040"></a> `00bcf040` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcf044"></a> `00bcf044` | `02 01 08 91` | add x2,x8,#0x200 | `FALL_THROUGH`
<a id="insn-00bcf048"></a> `00bcf048` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcf04c"></a> `00bcf04c` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bcf050"></a> `00bcf050` | `0c 3a 02 94` | bl 0x00c5d880 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf054"></a> `00bcf054` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcf058"></a> `00bcf058` | `6e 2d 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf05c"></a> `00bcf05c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf060"></a> `00bcf060` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf064"></a> `00bcf064` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcf068"></a> `00bcf068` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bceff0`](#insn-00bceff0) 範囲 `[['00bceff0', '00bcf06b']]`

## 命令位置別の参照

- [`00bceff0`](#insn-00bceff0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceff4`](#insn-00bceff4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceff8`](#insn-00bceff8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf00c`](#insn-00bcf00c) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bcf018`](#insn-00bcf018) → `01126380`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcf024`](#insn-00bcf024) → [`00574cac`](../00574/00574cac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574cac` · 推定シンボル `None` · 推定型 `None`
- [`00bcf02c`](#insn-00bcf02c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcf03c`](#insn-00bcf03c) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcf050`](#insn-00bcf050) → [`00c5d880`](../00c5d/00c5d880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d880` · 推定シンボル `None` · 推定型 `None`
- [`00bcf058`](#insn-00bcf058) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcf05c`](#insn-00bcf05c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf060`](#insn-00bcf060) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bceff0`](#insn-00bceff0)

~~~json
{
  "source": "00bceff0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceff4`](#insn-00bceff4)

~~~json
{
  "source": "00bceff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceff8`](#insn-00bceff8)

~~~json
{
  "source": "00bceff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf00c`](#insn-00bcf00c)

~~~json
{
  "source": "00bcf00c",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf018`](#insn-00bcf018)

~~~json
{
  "source": "00bcf018",
  "target": "01126380",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126380",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcf024`](#insn-00bcf024)

~~~json
{
  "source": "00bcf024",
  "target": "00574cac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf02c`](#insn-00bcf02c)

~~~json
{
  "source": "00bcf02c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf03c`](#insn-00bcf03c)

~~~json
{
  "source": "00bcf03c",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf050`](#insn-00bcf050)

~~~json
{
  "source": "00bcf050",
  "target": "00c5d880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf058`](#insn-00bcf058)

~~~json
{
  "source": "00bcf058",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf05c`](#insn-00bcf05c)

~~~json
{
  "source": "00bcf05c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf060`](#insn-00bcf060)

~~~json
{
  "source": "00bcf060",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
