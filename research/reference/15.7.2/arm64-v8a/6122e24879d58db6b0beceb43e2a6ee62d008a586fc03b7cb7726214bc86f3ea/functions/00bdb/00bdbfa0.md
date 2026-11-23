# 00bdbfa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdc050`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc050.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-f2867635b4f9ebd821e7375503b7ad49)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbfa0",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d947057bae6371209a989bf16bf78b782025af60b38b8cdca651a30a67d056d6",
  "source_text_sha256": "d947057bae6371209a989bf16bf78b782025af60b38b8cdca651a30a67d056d6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbfa0",
        "00bdbfaf"
      ]
    ],
    "bytes_sha256": "b77ed1ecf5602d353a53fdf364be5d04ed22945cfbaf923066bacf470ca9a171",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004a33f8](../004a3/004a33f8.md)
- [00b31d40](../00b31/00b31d40.md)
- [00b382ec](../00b38/00b382ec.md)
- [00b384c0](../00b38/00b384c0.md)
- [00b38674](../00b38/00b38674.md)
- [00b38828](../00b38/00b38828.md)
- [00b3f8f8](../00b3f/00b3f8f8.md)
- [00b4127c](../00b41/00b4127c.md)
- [00b41450](../00b41/00b41450.md)
- [00b46650](../00b46/00b46650.md)
- [00b46a88](../00b46/00b46a88.md)
- [00b46b54](../00b46/00b46b54.md)
- [00b46c00](../00b46/00b46c00.md)
- [00b46f84](../00b46/00b46f84.md)
- [00b7f24c](../00b7f/00b7f24c.md)
- [00b819f8](../00b81/00b819f8.md)
- [00b897b0](../00b89/00b897b0.md)

## 呼び出し先

- [00b31d40](../00b31/00b31d40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 175 bytes

~~~c

void _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv(void)

{
  (*(code *)PTR__ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv_00c1c808)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbfa0"></a> `00bdbfa0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbfa4"></a> `00bdbfa4` | `11 06 44 f9` | ldr x17,[x16, #0x808] | `FALL_THROUGH`
<a id="insn-00bdbfa8"></a> `00bdbfa8` | `10 22 20 91` | add x16,x16,#0x808 | `FALL_THROUGH`
<a id="insn-00bdbfac"></a> `00bdbfac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbfa0`](#insn-00bdbfa0) 範囲 `[['00bdbfa0', '00bdbfaf']]`

## 命令位置別の参照

- [`00bdbfa4`](#insn-00bdbfa4) → `00c1c808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbfac`](#insn-00bdbfac) → [`00b31d40`](../00b31/00b31d40.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b31d40` · 推定シンボル `_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbfa4`](#insn-00bdbfa4)

~~~json
{
  "source": "00bdbfa4",
  "target": "00c1c808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbfac`](#insn-00bdbfac)

~~~json
{
  "source": "00bdbfac",
  "target": "00b31d40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
