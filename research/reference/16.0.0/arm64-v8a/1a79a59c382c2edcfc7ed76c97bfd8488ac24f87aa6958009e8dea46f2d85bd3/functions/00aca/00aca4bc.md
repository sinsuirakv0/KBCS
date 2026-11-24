# 00aca4bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6c528`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c528.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/no_difference_in_scope-0008.md#compare-24cddda298fc2af01e1870c567492672)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aca6b8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00aca6b8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/no_difference_in_scope-0012.md#compare-5c48446003655d5be477025925efc264)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca4bc",
  "name": "FUN_00aca4bc",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8fb8009f2be3fa5e2ec23b593376268ed3c52ed207722452b4371a2ff546171",
  "source_text_sha256": "d8fb8009f2be3fa5e2ec23b593376268ed3c52ed207722452b4371a2ff546171",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aca4bc",
        "00aca4cb"
      ]
    ],
    "bytes_sha256": "2cd2e5e65e1e4a860e2efd36ba59953aa463f71d0addf9c7942ec9b05562f2b8",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [00a79a0c](../00a79/00a79a0c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [00ac9580](../00ac9/00ac9580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 128 bytes

~~~c

void FUN_00aca4bc(long param_1)

{
  if (*(char *)(param_1 + 0x3c) != '\0') {
    FUN_00ac9580();
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aca4bc"></a> `00aca4bc` | `08 f0 40 39` | ldrb w8,[x0, #0x3c] | `FALL_THROUGH`
<a id="insn-00aca4c0"></a> `00aca4c0` | `48 00 00 34` | cbz w8,0x00aca4c8 | `CONDITIONAL_JUMP`
<a id="insn-00aca4c4"></a> `00aca4c4` | `2f fc ff 17` | b 0x00ac9580 | `CALL_TERMINATOR`
<a id="insn-00aca4c8"></a> `00aca4c8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aca4bc`](#insn-00aca4bc) 範囲 `[['00aca4bc', '00aca4c3']]`
  - `CONDITIONAL_JUMP` [`00aca4c0`](#insn-00aca4c0) → [`00aca4c8`](#insn-00aca4c8)
  - `FALL_THROUGH` [`00aca4c0`](#insn-00aca4c0) → [`00aca4c4`](#insn-00aca4c4)
- ブロック [`00aca4c4`](#insn-00aca4c4) 範囲 `[['00aca4c4', '00aca4c7']]`
- ブロック [`00aca4c8`](#insn-00aca4c8) 範囲 `[['00aca4c8', '00aca4cb']]`

## 命令位置別の参照

- [`00aca4c0`](#insn-00aca4c0) → [`00aca4c8`](#insn-00aca4c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aca4c4`](#insn-00aca4c4) → [`00ac9580`](../00ac9/00ac9580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac9580` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aca4c0`](#insn-00aca4c0)

~~~json
{
  "source": "00aca4c0",
  "target": "00aca4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aca4c4`](#insn-00aca4c4)

~~~json
{
  "source": "00aca4c4",
  "target": "00ac9580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
