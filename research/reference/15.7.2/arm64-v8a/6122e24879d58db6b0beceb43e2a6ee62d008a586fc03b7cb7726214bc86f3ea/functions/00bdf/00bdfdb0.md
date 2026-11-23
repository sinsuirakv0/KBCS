# 00bdfdb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfe60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0021.md#compare-2541ce6ba23a5c394638fb6caf459e0c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfdb0",
  "name": "_ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1f7f6cd446dd0c1f50a52dcbf11527c440c307185ba39dfcf99918248c29f0d4",
  "source_text_sha256": "1f7f6cd446dd0c1f50a52dcbf11527c440c307185ba39dfcf99918248c29f0d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfdb0",
        "00bdfdbf"
      ]
    ],
    "bytes_sha256": "4ab9564c95d4defcd03bfe58d361ca0e3e3773291f7ab5b712add0422c9f487d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b217a4](../00b21/00b217a4.md)
- [00b42fb4](../00b42/00b42fb4.md)

## 呼び出し先

- [00b42fb4](../00b42/00b42fb4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 296 bytes

~~~c

void _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_(void)

{
                    /* try { // try from 00bdfdb0 to 00cdff63 has its CatchHandler @ 00bdfbd4 */
  (*(code *)PTR__ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T__00c1e710)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfdb0"></a> `00bdfdb0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfdb4"></a> `00bdfdb4` | `11 8a 43 f9` | ldr x17,[x16, #0x710] | `FALL_THROUGH`
<a id="insn-00bdfdb8"></a> `00bdfdb8` | `10 42 1c 91` | add x16,x16,#0x710 | `FALL_THROUGH`
<a id="insn-00bdfdbc"></a> `00bdfdbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfdb0`](#insn-00bdfdb0) 範囲 `[['00bdfdb0', '00bdfdbf']]`

## 命令位置別の参照

- [`00bdfdb4`](#insn-00bdfdb4) → `00c1e710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfdbc`](#insn-00bdfdbc) → [`00b42fb4`](../00b42/00b42fb4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b42fb4` · 推定シンボル `_ZNSt6__ndk16__sortIRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfdb4`](#insn-00bdfdb4)

~~~json
{
  "source": "00bdfdb4",
  "target": "00c1e710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e710",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfdbc`](#insn-00bdfdbc)

~~~json
{
  "source": "00bdfdbc",
  "target": "00b42fb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
