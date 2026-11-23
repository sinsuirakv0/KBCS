# 00bddda0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdde50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-f9cc104e7255fe6ab82fa5d270561e6e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddda0",
  "name": "_ZN8firebase9analytics8internal38UnregisterTerminateOnDefaultAppDestroyEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ceac04ae86687f995b3f9a966ca7f18a043134ca98cb50db12cda8e6f8d3d03",
  "source_text_sha256": "2ceac04ae86687f995b3f9a966ca7f18a043134ca98cb50db12cda8e6f8d3d03",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddda0",
        "00bdddaf"
      ]
    ],
    "bytes_sha256": "7dca9241a8f05d1753a0a896503943c5d803796cdba1586668f12fe903e16549",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae124c](../00ae1/00ae124c.md)

## 呼び出し先

- [00ae00b4](../00ae0/00ae00b4.md)

## 関連文字列（未確認候補）

~~~text
"´®"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 218 bytes

~~~c

void _ZN8firebase9analytics8internal38UnregisterTerminateOnDefaultAppDestroyEv(void)

{
  (*(code *)PTR__ZN8firebase9analytics8internal38UnregisterTerminateOnDefaultAppDestroyEv_00c1d708)
            ();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddda0"></a> `00bddda0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddda4"></a> `00bddda4` | `11 86 43 f9` | ldr x17,[x16, #0x708] | `FALL_THROUGH`
<a id="insn-00bddda8"></a> `00bddda8` | `10 22 1c 91` | add x16,x16,#0x708 | `FALL_THROUGH`
<a id="insn-00bdddac"></a> `00bdddac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddda0`](#insn-00bddda0) 範囲 `[['00bddda0', '00bdddaf']]`

## 命令位置別の参照

- [`00bddda4`](#insn-00bddda4) → `00c1d708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddac`](#insn-00bdddac) → [`00ae00b4`](../00ae0/00ae00b4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae00b4` · 推定シンボル `_ZN8firebase9analytics8internal38UnregisterTerminateOnDefaultAppDestroyEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddda4`](#insn-00bddda4)

~~~json
{
  "source": "00bddda4",
  "target": "00c1d708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d708",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddac`](#insn-00bdddac)

~~~json
{
  "source": "00bdddac",
  "target": "00ae00b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
