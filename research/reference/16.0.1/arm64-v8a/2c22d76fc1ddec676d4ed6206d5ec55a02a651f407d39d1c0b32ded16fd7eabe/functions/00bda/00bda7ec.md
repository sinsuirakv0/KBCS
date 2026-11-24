# 00bda7ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bda3c4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bda/00bda3c4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-7dee335f5822380e6d75e40b53a27043)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bda888`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bda/00bda888.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-9e028feb0cef754c24a90c050df454a8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda7ec",
  "name": "_ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a81525bcda9f99b25970576ecd2010e663e7053e802d3d68d6b82fbd325b3096",
  "source_text_sha256": "a81525bcda9f99b25970576ecd2010e663e7053e802d3d68d6b82fbd325b3096",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda7ec",
        "00bda81b"
      ]
    ],
    "bytes_sha256": "0a573371c438c17868317546075ac0e9c39fe4a0d98ad28dd613a3cc4636740b",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5de40](../00c5d/00c5de40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 254 bytes

~~~c

undefined8 *
_ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenaSERKS2_
          (undefined8 *param_1,undefined8 *param_2)

{
  _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject(*param_1,*(undefined8 *)*param_2);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bda7ec"></a> `00bda7ec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bda7f0"></a> `00bda7f0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda7f4"></a> `00bda7f4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bda7f8"></a> `00bda7f8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bda7fc"></a> `00bda7fc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bda800"></a> `00bda800` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bda804"></a> `00bda804` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00bda808"></a> `00bda808` | `8e 0d 02 94` | bl 0x00c5de40 | `UNCONDITIONAL_CALL`
<a id="insn-00bda80c"></a> `00bda80c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda810"></a> `00bda810` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bda814"></a> `00bda814` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bda818"></a> `00bda818` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bda7ec`](#insn-00bda7ec) 範囲 `[['00bda7ec', '00bda81b']]`

## 命令位置別の参照

- [`00bda7ec`](#insn-00bda7ec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7f0`](#insn-00bda7f0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda808`](#insn-00bda808) → [`00c5de40`](../00c5d/00c5de40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de40` · 推定シンボル `None` · 推定型 `None`
- [`00bda80c`](#insn-00bda80c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda7ec`](#insn-00bda7ec)

~~~json
{
  "source": "00bda7ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7f0`](#insn-00bda7f0)

~~~json
{
  "source": "00bda7f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda808`](#insn-00bda808)

~~~json
{
  "source": "00bda808",
  "target": "00c5de40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda80c`](#insn-00bda80c)

~~~json
{
  "source": "00bda80c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
