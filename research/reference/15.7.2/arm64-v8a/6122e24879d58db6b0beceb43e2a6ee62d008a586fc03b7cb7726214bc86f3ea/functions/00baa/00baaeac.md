# 00baaeac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baaf74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baaf74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0044.md#compare-dfa13de1bcf37d291ece4458a09b1692)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baaeac",
  "name": "_ZNKSt6__ndk112ctype_bynameIwE10do_toupperEw",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "84ac7bc31c266b3a170f5cb24f7a8a4fd0ca4633baa57a04de051e811182cfbd",
  "source_text_sha256": "84ac7bc31c266b3a170f5cb24f7a8a4fd0ca4633baa57a04de051e811182cfbd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baaeac",
        "00baaebf"
      ]
    ],
    "bytes_sha256": "96bb22de9e970fb3e35d54f3d8cba384ec8461fa9f9e6e6da7f5ac5c1e6a0b15",
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

- [00be19e0](../00be1/00be19e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 186 bytes

~~~c

wint_t _ZNKSt6__ndk112ctype_bynameIwE10do_toupperEw(long param_1,wint_t param_2)

{
  wint_t wVar1;
  
  wVar1 = towupper_l(param_2,*(__locale_t *)(param_1 + 0x10));
  return wVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baaeac"></a> `00baaeac` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baaeb0"></a> `00baaeb0` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00baaeb4"></a> `00baaeb4` | `e0 03 01 2a` | mov w0,w1 | `FALL_THROUGH`
<a id="insn-00baaeb8"></a> `00baaeb8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00baaebc"></a> `00baaebc` | `c9 da 00 14` | b 0x00be19e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baaeac`](#insn-00baaeac) 範囲 `[['00baaeac', '00baaebf']]`

## 命令位置別の参照

- [`00baaebc`](#insn-00baaebc) → [`00be19e0`](../00be1/00be19e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be19e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baaebc`](#insn-00baaebc)

~~~json
{
  "source": "00baaebc",
  "target": "00be19e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
