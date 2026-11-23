# 00baafe4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baaf1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baa/00baaf1c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0044.md#compare-ec85a3959b19f49ef835fcdc89dbf183)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bab028`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab028.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/machine_only_observed-0043.md#compare-968a19629ddd1f38eda351c062341655)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baafe4",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEw",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28f80e5a3fb3b3f6a405f54888dd37d0634cb68ba9fdb110b4e705e7da43af5f",
  "source_text_sha256": "28f80e5a3fb3b3f6a405f54888dd37d0634cb68ba9fdb110b4e705e7da43af5f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baafe4",
        "00baaff7"
      ]
    ],
    "bytes_sha256": "c746f9b73bfb49cbf0adb9163487b7c28fabdaec1079e88f13da414f6a79a53a",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1aa0](../00be1/00be1aa0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 186 bytes

~~~c

wint_t _ZNKSt6__ndk112ctype_bynameIwE10do_tolowerEw(long param_1,wint_t param_2)

{
  wint_t wVar1;
  
  wVar1 = towlower_l(param_2,*(__locale_t *)(param_1 + 0x10));
  return wVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baafe4"></a> `00baafe4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baafe8"></a> `00baafe8` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baafec"></a> `00baafec` | `e0 03 01 2a` | mov w0,w1 | `FALL_THROUGH`
<a id="insn-00baaff0"></a> `00baaff0` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00baaff4"></a> `00baaff4` | `ab da 00 14` | b 0x00be1aa0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baafe4`](#insn-00baafe4) 範囲 `[['00baafe4', '00baaff7']]`

## 命令位置別の参照

- [`00baaff4`](#insn-00baaff4) → [`00be1aa0`](../00be1/00be1aa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1aa0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaff4`](#insn-00baaff4)

~~~json
{
  "source": "00baaff4",
  "target": "00be1aa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
