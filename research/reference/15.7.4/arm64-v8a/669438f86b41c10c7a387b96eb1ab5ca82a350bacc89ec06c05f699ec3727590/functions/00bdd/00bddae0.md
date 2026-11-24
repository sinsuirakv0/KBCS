# 00bddae0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdda90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0017.md#compare-e9d53c691d3cab06f38f79de4c18045b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a530`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a530.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-1c2df571d51fd144fa02ea2f2e52f329)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddae0",
  "name": "<EXTERNAL>::atoi",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "501d8539eefe3e735eabf2255a9ffc5fb9e84ac9e10e75bd38157f3546ca59cf",
  "source_text_sha256": "501d8539eefe3e735eabf2255a9ffc5fb9e84ac9e10e75bd38157f3546ca59cf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddae0",
        "00bddaef"
      ]
    ],
    "bytes_sha256": "be63fd21314255c2030a87338304d98acb61bd480bd1a7e1173357117a8dfe51",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007e5fa4](../007e5/007e5fa4.md)
- [00b12820](../00b12/00b12820.md)
- [00b17160](../00b17/00b17160.md)
- [00b18d1c](../00b18/00b18d1c.md)
- [00b195a8](../00b19/00b195a8.md)
- [00b218b0](../00b21/00b218b0.md)
- [00b22320](../00b22/00b22320.md)

## 呼び出し先

- [010a5560](../010a5/010a5560.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 193 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int atoi(char *__nptr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_atoi_00c1d628)((int)__nptr);
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddae0"></a> `00bddae0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddae4"></a> `00bddae4` | `11 16 43 f9` | ldr x17,[x16, #0x628] | `FALL_THROUGH`
<a id="insn-00bddae8"></a> `00bddae8` | `10 a2 18 91` | add x16,x16,#0x628 | `FALL_THROUGH`
<a id="insn-00bddaec"></a> `00bddaec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddae0`](#insn-00bddae0) 範囲 `[['00bddae0', '00bddaef']]`

## 命令位置別の参照

- [`00bddae4`](#insn-00bddae4) → `00c1d628`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddaec`](#insn-00bddaec) → [`010a5560`](../010a5/010a5560.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5560` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddae4`](#insn-00bddae4)

~~~json
{
  "source": "00bddae4",
  "target": "00c1d628",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d628",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddaec`](#insn-00bddaec)

~~~json
{
  "source": "00bddaec",
  "target": "010a5560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
