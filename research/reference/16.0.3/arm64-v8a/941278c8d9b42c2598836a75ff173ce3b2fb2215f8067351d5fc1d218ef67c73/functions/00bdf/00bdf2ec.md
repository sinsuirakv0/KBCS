# 00bdf2ec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bde2f8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde2f8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-166145712358c8b42d9556a7e96a03a4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf2ec",
  "name": "_ZN8firebase4auth4UserD2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a10af5a179236e6719a8c7bd5cdad893733a77809ad6b3d76b89b4e9c4567df4",
  "source_text_sha256": "a10af5a179236e6719a8c7bd5cdad893733a77809ad6b3d76b89b4e9c4567df4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdf2ec",
        "00bdf303"
      ]
    ],
    "bytes_sha256": "9a972a1ef11482e84b86decb50206ac3eb1136e8fc904287af6df242cc7c458f",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5baf0](../00c5b/00c5baf0.md)

## 呼び出し先

- [00c5ec20](../00c5e/00c5ec20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 242 bytes

~~~c

void _ZN8firebase4auth4UserD2Ev(long *param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR__ZTVN8firebase4auth4UserE_00c9ca60;
  param_1[0x13] = 0;
  *param_1 = (long)(puVar1 + 0x10);
  _ZN8firebase4auth17UserInfoInterfaceD2Ev();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdf2ec"></a> `00bdf2ec` | `e8 05 00 b0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bdf2f0"></a> `00bdf2f0` | `08 31 45 f9` | ldr x8,[x8, #0xa60] | `FALL_THROUGH`
<a id="insn-00bdf2f4"></a> `00bdf2f4` | `1f 4c 00 f9` | str xzr,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bdf2f8"></a> `00bdf2f8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bdf2fc"></a> `00bdf2fc` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdf300"></a> `00bdf300` | `48 fe 01 14` | b 0x00c5ec20 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdf2ec`](#insn-00bdf2ec) 範囲 `[['00bdf2ec', '00bdf303']]`

## 命令位置別の参照

- [`00bdf2f0`](#insn-00bdf2f0) → `00c9ca60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdf2fc`](#insn-00bdf2fc) → `00c93948`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[80]`
- [`00bdf300`](#insn-00bdf300) → [`00c5ec20`](../00c5e/00c5ec20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ec20` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdf2f0`](#insn-00bdf2f0)

~~~json
{
  "source": "00bdf2f0",
  "target": "00c9ca60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdf2fc`](#insn-00bdf2fc)

~~~json
{
  "source": "00bdf2fc",
  "target": "00c93948",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93938",
  "offset": 16,
  "size": 80,
  "datatype": "undefined1[80]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00bdf300`](#insn-00bdf300)

~~~json
{
  "source": "00bdf300",
  "target": "00c5ec20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
