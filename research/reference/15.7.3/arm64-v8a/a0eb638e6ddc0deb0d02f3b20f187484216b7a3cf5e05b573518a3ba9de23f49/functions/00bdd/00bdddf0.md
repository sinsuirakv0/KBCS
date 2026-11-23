# 00bdddf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddd40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-806c35e40f4d7e809c6dd9081bc54426)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdde40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-56752fc75d9577e894eacc7f96bac037)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddf0",
  "name": "_ZN8firebase8LogErrorEPKcz",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d75727f1a5b49479783879b4eeaf4a30b9cf1be38b5e0276c06d9fc843a2f50d",
  "source_text_sha256": "d75727f1a5b49479783879b4eeaf4a30b9cf1be38b5e0276c06d9fc843a2f50d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddf0",
        "00bdddff"
      ]
    ],
    "bytes_sha256": "fd42c33e27925947ebb74012be34cd9c61b8b78f8aa20e0af6c4104631b5dccc",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae053c](../00ae0/00ae053c.md)
- [00ae14f0](../00ae1/00ae14f0.md)
- [00ae1b1c](../00ae1/00ae1b1c.md)
- [00ae1c20](../00ae1/00ae1c20.md)
- [00ae210c](../00ae2/00ae210c.md)
- [00ae2290](../00ae2/00ae2290.md)
- [00ae23e8](../00ae2/00ae23e8.md)
- [00ae2554](../00ae2/00ae2554.md)
- [00ae26dc](../00ae2/00ae26dc.md)
- [00ae2920](../00ae2/00ae2920.md)
- [00ae2a24](../00ae2/00ae2a24.md)
- [00ae2f90](../00ae2/00ae2f90.md)
- [00ae3a08](../00ae3/00ae3a08.md)
- [00ae4748](../00ae4/00ae4748.md)
- [00ae4b54](../00ae4/00ae4b54.md)
- [00ae4e6c](../00ae4/00ae4e6c.md)
- [00af0d0c](../00af0/00af0d0c.md)
- [00b02854](../00b02/00b02854.md)
- [00b02e7c](../00b02/00b02e7c.md)
- [00b0347c](../00b03/00b0347c.md)
- [00b0357c](../00b03/00b0357c.md)
- [00b03610](../00b03/00b03610.md)
- [00b03728](../00b03/00b03728.md)
- [00b03ca4](../00b03/00b03ca4.md)
- [00b04510](../00b04/00b04510.md)
- [00b04570](../00b04/00b04570.md)
- [00b045c4](../00b04/00b045c4.md)
- [00b04630](../00b04/00b04630.md)
- [00b06be8](../00b06/00b06be8.md)
- [00b06ce0](../00b06/00b06ce0.md)
- [00b08098](../00b08/00b08098.md)
- [00b0871c](../00b08/00b0871c.md)
- [00b0a968](../00b0a/00b0a968.md)
- [00b0d740](../00b0d/00b0d740.md)
- [00b494c8](../00b49/00b494c8.md)
- [00b4c480](../00b4c/00b4c480.md)
- [00b4cbfc](../00b4c/00b4cbfc.md)
- [00b4cd3c](../00b4c/00b4cd3c.md)
- [00b4cda8](../00b4c/00b4cda8.md)
- [00b4ce90](../00b4c/00b4ce90.md)
- [00b4d204](../00b4d/00b4d204.md)
- [00b4d7a8](../00b4d/00b4d7a8.md)
- [00b4de04](../00b4d/00b4de04.md)
- [00b4e440](../00b4e/00b4e440.md)
- [00b4ee88](../00b4e/00b4ee88.md)
- [00b573f4](../00b57/00b573f4.md)
- [00b58600](../00b58/00b58600.md)
- [00b586f4](../00b58/00b586f4.md)
- [00b588ac](../00b58/00b588ac.md)
- [00b589a0](../00b58/00b589a0.md)
- [00b58aa0](../00b58/00b58aa0.md)
- [00b58c10](../00b58/00b58c10.md)
- [00b5906c](../00b59/00b5906c.md)
- [00b69ab8](../00b69/00b69ab8.md)
- [00b69f14](../00b69/00b69f14.md)
- [00b6a060](../00b6a/00b6a060.md)
- [00b6a1ac](../00b6a/00b6a1ac.md)
- [00b6a350](../00b6a/00b6a350.md)
- [00b6a49c](../00b6a/00b6a49c.md)
- [00b6a620](../00b6a/00b6a620.md)
- [00b6a7e4](../00b6a/00b6a7e4.md)
- [00b6b64c](../00b6b/00b6b64c.md)

## 呼び出し先

- [00ae4280](../00ae4/00ae4280.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 111 bytes

~~~c

void _ZN8firebase8LogErrorEPKcz(void)

{
  (*(code *)PTR__ZN8firebase8LogErrorEPKcz_00c1d788)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddf0"></a> `00bdddf0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdddf4"></a> `00bdddf4` | `11 c6 43 f9` | ldr x17,[x16, #0x788] | `FALL_THROUGH`
<a id="insn-00bdddf8"></a> `00bdddf8` | `10 22 1e 91` | add x16,x16,#0x788 | `FALL_THROUGH`
<a id="insn-00bdddfc"></a> `00bdddfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddf0`](#insn-00bdddf0) 範囲 `[['00bdddf0', '00bdddff']]`

## 命令位置別の参照

- [`00bdddf4`](#insn-00bdddf4) → `00c1d788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdddfc`](#insn-00bdddfc) → [`00ae4280`](../00ae4/00ae4280.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae4280` · 推定シンボル `_ZN8firebase8LogErrorEPKcz` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddf4`](#insn-00bdddf4)

~~~json
{
  "source": "00bdddf4",
  "target": "00c1d788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d788",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdddfc`](#insn-00bdddfc)

~~~json
{
  "source": "00bdddfc",
  "target": "00ae4280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
