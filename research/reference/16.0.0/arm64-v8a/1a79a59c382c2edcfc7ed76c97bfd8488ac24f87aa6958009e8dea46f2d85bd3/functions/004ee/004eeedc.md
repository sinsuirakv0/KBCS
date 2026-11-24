# 004eeedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004cc044`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004cc/004cc044.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/reference_unresolved-0001.md#compare-302426cd93d93a9d5c89fd9b743de193)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004eef1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ee/004eef1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/reference_unresolved-0001.md#compare-90c6902995b5057ac1fe021335b0485e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004eeedc",
  "name": "_ZN5Botan16PK_Encryptor_EMED1Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ca601376976c4f28be4fbe15f8d152d110ba0dd001586732c2ab871d6a9e384",
  "source_text_sha256": "0ca601376976c4f28be4fbe15f8d152d110ba0dd001586732c2ab871d6a9e384",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004eeedc",
        "004eeefb"
      ]
    ],
    "bytes_sha256": "f14671fb398467de3ee15392d473c437b600e4f2b39631b4efbff75737664520",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c58e10](../00c58/00c58e10.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 405 bytes

~~~c

void _ZN5Botan16PK_Encryptor_EMED1Ev(long param_1)

{
  long *plVar1;
  
  plVar1 = *(long **)(param_1 + 8);
  *(undefined8 *)(param_1 + 8) = 0;
  if (plVar1 != (long *)0x0) {
                    /* WARNING: Could not recover jumptable at 0x004eeef4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*plVar1 + 0x18))();
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004eeedc"></a> `004eeedc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-004eeee0"></a> `004eeee0` | `00 04 40 f9` | ldr x0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004eeee4"></a> `004eeee4` | `1f 05 00 f9` | str xzr,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-004eeee8"></a> `004eeee8` | `80 00 00 b4` | cbz x0,0x004eeef8 | `CONDITIONAL_JUMP`
<a id="insn-004eeeec"></a> `004eeeec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004eeef0"></a> `004eeef0` | `01 0d 40 f9` | ldr x1,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-004eeef4"></a> `004eeef4` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-004eeef8"></a> `004eeef8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004eeedc`](#insn-004eeedc) 範囲 `[['004eeedc', '004eeeeb']]`
  - `CONDITIONAL_JUMP` [`004eeee8`](#insn-004eeee8) → [`004eeef8`](#insn-004eeef8)
  - `FALL_THROUGH` [`004eeee8`](#insn-004eeee8) → [`004eeeec`](#insn-004eeeec)
- ブロック [`004eeeec`](#insn-004eeeec) 範囲 `[['004eeeec', '004eeef7']]`
- ブロック [`004eeef8`](#insn-004eeef8) 範囲 `[['004eeef8', '004eeefb']]`

## 命令位置別の参照

- [`004eeee8`](#insn-004eeee8) → [`004eeef8`](#insn-004eeef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004eeee8`](#insn-004eeee8)

~~~json
{
  "source": "004eeee8",
  "target": "004eeef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
