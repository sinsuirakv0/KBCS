# 00bcdbe0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcdb44`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdb44.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-0aac71bafda61eade9dcac944fbea93f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcebd4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcebd4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-ba6b4d5dbd17d99ecc66e7d4ad32adeb)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdbe0",
  "name": "_ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d64db83b8c79c9db5c7abee8fe01970f654e1d4a20cd54a361ba6bb0470c8293",
  "source_text_sha256": "d64db83b8c79c9db5c7abee8fe01970f654e1d4a20cd54a361ba6bb0470c8293",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdbe0",
        "00bcdc07"
      ]
    ],
    "bytes_sha256": "f2f992b8e315834379abf6923bd90b0c967c7737884666a68c5818968c02cc70",
    "instruction_count": 10,
    "instruction_bytes": 40,
    "body_bytes": 40,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5dae0](../00c5d/00c5dae0.md)
- [00c5dd00](../00c5d/00c5dd00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 319 bytes

~~~c

void _ZN8firebase4auth45JniAuthStateListener_nativeOnAuthStateChangedEP7_JNIEnvP8_jobjectl
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE(param_3);
  _ZN8firebase4auth24NotifyAuthStateListenersEPNS0_8AuthDataE(param_3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdbe0"></a> `00bcdbe0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcdbe4"></a> `00bcdbe4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdbe8"></a> `00bcdbe8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdbec"></a> `00bcdbec` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bcdbf0"></a> `00bcdbf0` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bcdbf4"></a> `00bcdbf4` | `43 40 02 94` | bl 0x00c5dd00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdbf8"></a> `00bcdbf8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdbfc"></a> `00bcdbfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdc00"></a> `00bcdc00` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcdc04"></a> `00bcdc04` | `b7 3f 02 14` | b 0x00c5dae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdbe0`](#insn-00bcdbe0) 範囲 `[['00bcdbe0', '00bcdc07']]`

## 命令位置別の参照

- [`00bcdbe0`](#insn-00bcdbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbe4`](#insn-00bcdbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbf4`](#insn-00bcdbf4) → [`00c5dd00`](../00c5d/00c5dd00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbf8`](#insn-00bcdbf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc04`](#insn-00bcdc04) → [`00c5dae0`](../00c5d/00c5dae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdbe0`](#insn-00bcdbe0)

~~~json
{
  "source": "00bcdbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbe4`](#insn-00bcdbe4)

~~~json
{
  "source": "00bcdbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbf4`](#insn-00bcdbf4)

~~~json
{
  "source": "00bcdbf4",
  "target": "00c5dd00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdbf8`](#insn-00bcdbf8)

~~~json
{
  "source": "00bcdbf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc04`](#insn-00bcdc04)

~~~json
{
  "source": "00bcdc04",
  "target": "00c5dae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
