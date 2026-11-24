# 00b0cecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0171.md#review-523c6e96c348b3d39b7af58deaec8be5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b0d2f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b0d/00b0d2f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-1965b6f0978b9f66c899b3b66e1938ae)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0cecc",
  "name": "FUN_00b0cecc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "256583e0ab5f7d7f2cb539fca4fe436018423e7245de8effc70dba737a675b76",
  "source_text_sha256": "256583e0ab5f7d7f2cb539fca4fe436018423e7245de8effc70dba737a675b76",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0cecc",
        "00b0cf13"
      ]
    ],
    "bytes_sha256": "3d7fcc2ab0010ba12ff4721eacc623667906f7dc04d2dbdb4302a20bef254667",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008514b8](../00851/008514b8.md)
- [008b6a18](../008b6/008b6a18.md)
- [008b7984](../008b7/008b7984.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 272 bytes

~~~c

void FUN_00b0cecc(void)

{
  long lVar1;
  undefined8 uVar2;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_008b7984(lVar1 + 0x2f38,0x329);
  FUN_008b6a18(uVar2,0);
  lVar1 = FUN_008514b8();
  uVar2 = FUN_008b7984(lVar1 + 0x2f38,0x32a);
  FUN_008b6a18(uVar2,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0cecc"></a> `00b0cecc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b0ced0"></a> `00b0ced0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0ced4"></a> `00b0ced4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b0ced8"></a> `00b0ced8` | `78 11 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cedc"></a> `00b0cedc` | `13 e7 85 52` | mov w19,#0x2f38 | `FALL_THROUGH`
<a id="insn-00b0cee0"></a> `00b0cee0` | `21 65 80 52` | mov w1,#0x329 | `FALL_THROUGH`
<a id="insn-00b0cee4"></a> `00b0cee4` | `00 00 13 8b` | add x0,x0,x19 | `FALL_THROUGH`
<a id="insn-00b0cee8"></a> `00b0cee8` | `a7 aa f6 97` | bl 0x008b7984 | `UNCONDITIONAL_CALL`
<a id="insn-00b0ceec"></a> `00b0ceec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b0cef0"></a> `00b0cef0` | `ca a6 f6 97` | bl 0x008b6a18 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cef4"></a> `00b0cef4` | `71 11 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cef8"></a> `00b0cef8` | `00 00 13 8b` | add x0,x0,x19 | `FALL_THROUGH`
<a id="insn-00b0cefc"></a> `00b0cefc` | `41 65 80 52` | mov w1,#0x32a | `FALL_THROUGH`
<a id="insn-00b0cf00"></a> `00b0cf00` | `a1 aa f6 97` | bl 0x008b7984 | `UNCONDITIONAL_CALL`
<a id="insn-00b0cf04"></a> `00b0cf04` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b0cf08"></a> `00b0cf08` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b0cf0c"></a> `00b0cf0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b0cf10"></a> `00b0cf10` | `c2 a6 f6 17` | b 0x008b6a18 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0cecc`](#insn-00b0cecc) 範囲 `[['00b0cecc', '00b0cf13']]`

## 命令位置別の参照

- [`00b0cecc`](#insn-00b0cecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ced0`](#insn-00b0ced0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ced8`](#insn-00b0ced8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00b0cee8`](#insn-00b0cee8) → [`008b7984`](../008b7/008b7984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7984` · 推定シンボル `None` · 推定型 `None`
- [`00b0cef0`](#insn-00b0cef0) → [`008b6a18`](../008b6/008b6a18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6a18` · 推定シンボル `None` · 推定型 `None`
- [`00b0cef4`](#insn-00b0cef4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf00`](#insn-00b0cf00) → [`008b7984`](../008b7/008b7984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b7984` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf08`](#insn-00b0cf08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf0c`](#insn-00b0cf0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0cf10`](#insn-00b0cf10) → [`008b6a18`](../008b6/008b6a18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008b6a18` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0cecc`](#insn-00b0cecc)

~~~json
{
  "source": "00b0cecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ced0`](#insn-00b0ced0)

~~~json
{
  "source": "00b0ced0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ced8`](#insn-00b0ced8)

~~~json
{
  "source": "00b0ced8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cee8`](#insn-00b0cee8)

~~~json
{
  "source": "00b0cee8",
  "target": "008b7984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cef0`](#insn-00b0cef0)

~~~json
{
  "source": "00b0cef0",
  "target": "008b6a18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cef4`](#insn-00b0cef4)

~~~json
{
  "source": "00b0cef4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cf00`](#insn-00b0cf00)

~~~json
{
  "source": "00b0cf00",
  "target": "008b7984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b0cf08`](#insn-00b0cf08)

~~~json
{
  "source": "00b0cf08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf0c`](#insn-00b0cf0c)

~~~json
{
  "source": "00b0cf0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0cf10`](#insn-00b0cf10)

~~~json
{
  "source": "00b0cf10",
  "target": "008b6a18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
