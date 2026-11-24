# 00ad4ffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad4fb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad4/00ad4fb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-37c1decc86203c1e190058ec929eb9fe)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0090.md#review-b9dce59554ff8a81c2482f7e4b1c3373)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad4ffc",
  "name": "FUN_00ad4ffc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fdb7e57ae151ec894e014a3457427577529a7fd7f999fe220a01bff496a35c85",
  "source_text_sha256": "fdb7e57ae151ec894e014a3457427577529a7fd7f999fe220a01bff496a35c85",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad4ffc",
        "00ad501f"
      ]
    ],
    "bytes_sha256": "bb9c08fdf04013f314d0cd6caac35ee098da6a810032369be769f05fe1fa6375",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 135 bytes

~~~c

void FUN_00ad4ffc(void)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  *puVar1 = &PTR_FUN_00c0f8c8;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad4ffc"></a> `00ad4ffc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00ad5000"></a> `00ad5000` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ad5004"></a> `00ad5004` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00ad5008"></a> `00ad5008` | `0e 18 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00ad500c"></a> `00ad500c` | `c8 09 00 d0` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00ad5010"></a> `00ad5010` | `08 21 23 91` | add x8,x8,#0x8c8 | `FALL_THROUGH`
<a id="insn-00ad5014"></a> `00ad5014` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad5018"></a> `00ad5018` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00ad501c"></a> `00ad501c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad4ffc`](#insn-00ad4ffc) 範囲 `[['00ad4ffc', '00ad501f']]`

## 命令位置別の参照

- [`00ad4ffc`](#insn-00ad4ffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad5008`](#insn-00ad5008) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00ad5014`](#insn-00ad5014) → `00c0f8c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ad5018`](#insn-00ad5018) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad4ffc`](#insn-00ad4ffc)

~~~json
{
  "source": "00ad4ffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad5008`](#insn-00ad5008)

~~~json
{
  "source": "00ad5008",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad5014`](#insn-00ad5014)

~~~json
{
  "source": "00ad5014",
  "target": "00c0f8c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f8c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ad5018`](#insn-00ad5018)

~~~json
{
  "source": "00ad5018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
