# 00bbbaec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4dd90`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4dd90.md) · 移動量 `+0x6dd5c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0064.md#compare-ce512fb2015b4d2d2506a7fe300a8cea)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbbf14`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbbf14.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-aa64f912959307b30f8018a81004669b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbaec",
  "name": "_ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "673aef6f204e3647f264f76847b124ddede33a10b6be028dfd2fe297bc3e52ba",
  "source_text_sha256": "673aef6f204e3647f264f76847b124ddede33a10b6be028dfd2fe297bc3e52ba",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbaec",
        "00bbbb3f"
      ]
    ],
    "bytes_sha256": "79adb256ceee2c49d1af87b022200b4662b7f2bba2f715da7f56fb56a52ea015",
    "instruction_count": 21,
    "instruction_bytes": 84,
    "body_bytes": 84,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497a08](../00497/00497a08.md)
- [00c5ac80](../00c5a/00c5ac80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 406 bytes

~~~c

bool _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv(void)

{
  char cVar1;
  undefined8 uVar2;
  
  if (DAT_01125f60 != 0) {
    uVar2 = _ZNK8firebase3App9GetJNIEnvEv();
    cVar1 = FUN_00497a08(uVar2,DAT_01125f98,DAT_01125ee0);
                    /* try { // try from 00bbbb24 to 00cbbb2f has its CatchHandler @ 00bbc5b4 */
    return cVar1 != '\0';
  }
  return DAT_01126004 == 1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbaec"></a> `00bbbaec` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bbbaf0"></a> `00bbbaf0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbaf4"></a> `00bbbaf4` | `48 2b 00 d0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbbaf8"></a> `00bbbaf8` | `00 b1 47 f9` | ldr x0,[x8, #0xf60] | `FALL_THROUGH`
<a id="insn-00bbbafc"></a> `00bbbafc` | `60 01 00 b4` | cbz x0,0x00bbbb28 | `CONDITIONAL_JUMP`
<a id="insn-00bbbb00"></a> `00bbbb00` | `60 7c 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb04"></a> `00bbbb04` | `48 2b 00 d0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbbb08"></a> `00bbbb08` | `49 2b 00 d0` | adrp x9,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbbb0c"></a> `00bbbb0c` | `01 cd 47 f9` | ldr x1,[x8, #0xf98] | `FALL_THROUGH`
<a id="insn-00bbbb10"></a> `00bbbb10` | `22 71 47 f9` | ldr x2,[x9, #0xee0] | `FALL_THROUGH`
<a id="insn-00bbbb14"></a> `00bbbb14` | `bd 6f e3 97` | bl 0x00497a08 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb18"></a> `00bbbb18` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bbbb1c"></a> `00bbbb1c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bbbb20"></a> `00bbbb20` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbbb24"></a> `00bbbb24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbb28"></a> `00bbbb28` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbbb2c"></a> `00bbbb2c` | `08 05 40 b9` | ldr w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bbbb30"></a> `00bbbb30` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbb34"></a> `00bbbb34` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbbb38"></a> `00bbbb38` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bbbb3c"></a> `00bbbb3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbbaec`](#insn-00bbbaec) 範囲 `[['00bbbaec', '00bbbaff']]`
  - `CONDITIONAL_JUMP` [`00bbbafc`](#insn-00bbbafc) → [`00bbbb28`](#insn-00bbbb28)
  - `FALL_THROUGH` [`00bbbafc`](#insn-00bbbafc) → [`00bbbb00`](#insn-00bbbb00)
- ブロック [`00bbbb00`](#insn-00bbbb00) 範囲 `[['00bbbb00', '00bbbb23']]`
  - `FALL_THROUGH` [`00bbbb20`](#insn-00bbbb20) → [`00bbbb24`](#insn-00bbbb24)
- ブロック [`00bbbb24`](#insn-00bbbb24) 範囲 `[['00bbbb24', '00bbbb27']]`
- ブロック [`00bbbb28`](#insn-00bbbb28) 範囲 `[['00bbbb28', '00bbbb3f']]`

## 命令位置別の参照

- [`00bbbaec`](#insn-00bbbaec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbaf8`](#insn-00bbbaf8) → `01125f60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbafc`](#insn-00bbbafc) → [`00bbbb28`](#insn-00bbbb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb00`](#insn-00bbbb00) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb0c`](#insn-00bbbb0c) → `01125f98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbb10`](#insn-00bbbb10) → `01125ee0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbbb14`](#insn-00bbbb14) → [`00497a08`](../00497/00497a08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497a08` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb20`](#insn-00bbbb20) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb2c`](#insn-00bbbb2c) → `01126004`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bbbb38`](#insn-00bbbb38) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbaec`](#insn-00bbbaec)

~~~json
{
  "source": "00bbbaec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbaf8`](#insn-00bbbaf8)

~~~json
{
  "source": "00bbbaf8",
  "target": "01125f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbafc`](#insn-00bbbafc)

~~~json
{
  "source": "00bbbafc",
  "target": "00bbbb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb00`](#insn-00bbbb00)

~~~json
{
  "source": "00bbbb00",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb0c`](#insn-00bbbb0c)

~~~json
{
  "source": "00bbbb0c",
  "target": "01125f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbb10`](#insn-00bbbb10)

~~~json
{
  "source": "00bbbb10",
  "target": "01125ee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125ee0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbb14`](#insn-00bbbb14)

~~~json
{
  "source": "00bbbb14",
  "target": "00497a08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb20`](#insn-00bbbb20)

~~~json
{
  "source": "00bbbb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb2c`](#insn-00bbbb2c)

~~~json
{
  "source": "00bbbb2c",
  "target": "01126004",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126004",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbbb38`](#insn-00bbbb38)

~~~json
{
  "source": "00bbbb38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
