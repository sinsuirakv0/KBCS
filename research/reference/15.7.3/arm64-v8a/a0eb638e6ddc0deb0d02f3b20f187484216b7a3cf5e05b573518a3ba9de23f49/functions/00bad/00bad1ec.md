# 00bad1ec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bad124`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bad/00bad124.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0023.md#compare-a81b6cbc072181468f2fb766ecbe4147)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bad230`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bad/00bad230.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-1bf57ef939ec2688ee2fc2eeb58b09fe)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bad1ec",
  "name": "_ZNKSt6__ndk114__codecvt_utf8IwE9do_lengthER9mbstate_tPKcS5_m",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2257a8eacab42a049b6da488293332627991ff1d35bdadb3f1fc847b0d299014",
  "source_text_sha256": "2257a8eacab42a049b6da488293332627991ff1d35bdadb3f1fc847b0d299014",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bad1ec",
        "00bad20b"
      ]
    ],
    "bytes_sha256": "fc64f1e7739675560ae0cbc3c00e044254fca63b1e95b678090f2aafdd4e2357",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bacce8](../00bac/00bacce8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 327 bytes

~~~c

void _ZNKSt6__ndk114__codecvt_utf8IwE9do_lengthER9mbstate_tPKcS5_m
               (long param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5)

{
  FUN_00bacce8(param_3,param_4,param_5,*(undefined8 *)(param_1 + 0x18),
               *(undefined4 *)(param_1 + 0x20));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bad1ec"></a> `00bad1ec` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bad1f0"></a> `00bad1f0` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bad1f4"></a> `00bad1f4` | `e1 03 03 aa` | mov x1,x3 | `FALL_THROUGH`
<a id="insn-00bad1f8"></a> `00bad1f8` | `03 0c 40 f9` | ldr x3,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bad1fc"></a> `00bad1fc` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bad200"></a> `00bad200` | `e2 03 04 aa` | mov x2,x4 | `FALL_THROUGH`
<a id="insn-00bad204"></a> `00bad204` | `e4 03 08 2a` | mov w4,w8 | `FALL_THROUGH`
<a id="insn-00bad208"></a> `00bad208` | `b8 fe ff 17` | b 0x00bacce8 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bad1ec`](#insn-00bad1ec) 範囲 `[['00bad1ec', '00bad20b']]`

## 命令位置別の参照

- [`00bad208`](#insn-00bad208) → [`00bacce8`](../00bac/00bacce8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bacce8` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bad208`](#insn-00bad208)

~~~json
{
  "source": "00bad208",
  "target": "00bacce8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
