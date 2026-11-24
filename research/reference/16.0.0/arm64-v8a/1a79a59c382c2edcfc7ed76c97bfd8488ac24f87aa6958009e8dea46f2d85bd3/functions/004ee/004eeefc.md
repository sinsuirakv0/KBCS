# 004eeefc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004cc064`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc064.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0007.md#compare-d54beed540ec06127185886641d9ee6c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004eef3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eef3c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0007.md#compare-6cc997efd65eee081d28ce85438489ec)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004eeefc",
  "name": "_ZN5Botan16PK_Encryptor_EMED0Ev",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dad1dc2e42d1358f49c8256dc9a7466b0dec2b78a04270b7b04518b68e1e436c",
  "source_text_sha256": "dad1dc2e42d1358f49c8256dc9a7466b0dec2b78a04270b7b04518b68e1e436c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004eeefc",
        "004eef1f"
      ]
    ],
    "bytes_sha256": "d2e561549c237a34a1a2cf2e190d57330386b281d3c4101d50097b662dd467f0",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c58e10](../00c58/00c58e10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 125 bytes

~~~c

void _ZN5Botan16PK_Encryptor_EMED0Ev(void *param_1)

{
  _ZN5Botan16PK_Encryptor_EMED1Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004eeefc"></a> `004eeefc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-004eef00"></a> `004eef00` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004eef04"></a> `004eef04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004eef08"></a> `004eef08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004eef0c"></a> `004eef0c` | `c1 a7 1d 94` | bl 0x00c58e10 | `UNCONDITIONAL_CALL`
<a id="insn-004eef10"></a> `004eef10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004eef14"></a> `004eef14` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004eef18"></a> `004eef18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-004eef1c"></a> `004eef1c` | `e5 a2 1d 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004eeefc`](#insn-004eeefc) 範囲 `[['004eeefc', '004eef1f']]`

## 命令位置別の参照

- [`004eeefc`](#insn-004eeefc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eef00`](#insn-004eef00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eef0c`](#insn-004eef0c) → [`00c58e10`](../00c58/00c58e10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58e10` · 推定シンボル `None` · 推定型 `None`
- [`004eef14`](#insn-004eef14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eef18`](#insn-004eef18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004eef1c`](#insn-004eef1c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004eeefc`](#insn-004eeefc)

~~~json
{
  "source": "004eeefc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eef00`](#insn-004eef00)

~~~json
{
  "source": "004eef00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eef0c`](#insn-004eef0c)

~~~json
{
  "source": "004eef0c",
  "target": "00c58e10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004eef14`](#insn-004eef14)

~~~json
{
  "source": "004eef14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eef18`](#insn-004eef18)

~~~json
{
  "source": "004eef18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004eef1c`](#insn-004eef1c)

~~~json
{
  "source": "004eef1c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
