# 00bd1afc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd16d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd1/00bd16d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-7f722111a05f995db9da174f1661bac3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd1b98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1b98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-308ada06742144ebe70433c9fcd73ff0)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1afc",
  "name": "_ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4e5a56317268935c128be06556a0e16daf0ece7a09ab8ec6ffe456416d19bae2",
  "source_text_sha256": "4e5a56317268935c128be06556a0e16daf0ece7a09ab8ec6ffe456416d19bae2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1afc",
        "00bd1b3f"
      ]
    ],
    "bytes_sha256": "695a2e24769ab58c680d2be998f17d61e00eda22dc68602f7280d1b05b367e1a",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5af10](../00c5a/00c5af10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuthInvalidCredentialsException"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 604 bytes

~~~c

long _ZN8firebase4auth29invalid_credentials_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_01126928 == 0) {
    DAT_01126928 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/FirebaseAuthInvalidCredentialsException",
                              param_3);
  }
  return DAT_01126928;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1afc"></a> `00bd1afc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd1b00"></a> `00bd1b00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1b04"></a> `00bd1b04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd1b08"></a> `00bd1b08` | `b3 2a 00 b0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd1b0c"></a> `00bd1b0c` | `68 96 44 f9` | ldr x8,[x19, #0x928] | `FALL_THROUGH`
<a id="insn-00bd1b10"></a> `00bd1b10` | `08 01 00 b5` | cbnz x8,0x00bd1b30 | `CONDITIONAL_JUMP`
<a id="insn-00bd1b14"></a> `00bd1b14` | `43 b7 ff 90` | adrp x3,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bd1b18"></a> `00bd1b18` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00bd1b1c"></a> `00bd1b1c` | `63 38 32 91` | add x3,x3,#0xc8e | `FALL_THROUGH`
<a id="insn-00bd1b20"></a> `00bd1b20` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd1b24"></a> `00bd1b24` | `fb 24 02 94` | bl 0x00c5af10 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1b28"></a> `00bd1b28` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd1b2c"></a> `00bd1b2c` | `60 96 04 f9` | str x0,[x19, #0x928] | `FALL_THROUGH`
<a id="insn-00bd1b30"></a> `00bd1b30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1b34"></a> `00bd1b34` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd1b38"></a> `00bd1b38` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd1b3c"></a> `00bd1b3c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1afc`](#insn-00bd1afc) 範囲 `[['00bd1afc', '00bd1b13']]`
  - `CONDITIONAL_JUMP` [`00bd1b10`](#insn-00bd1b10) → [`00bd1b30`](#insn-00bd1b30)
  - `FALL_THROUGH` [`00bd1b10`](#insn-00bd1b10) → [`00bd1b14`](#insn-00bd1b14)
- ブロック [`00bd1b14`](#insn-00bd1b14) 範囲 `[['00bd1b14', '00bd1b2f']]`
  - `FALL_THROUGH` [`00bd1b2c`](#insn-00bd1b2c) → [`00bd1b30`](#insn-00bd1b30)
- ブロック [`00bd1b30`](#insn-00bd1b30) 範囲 `[['00bd1b30', '00bd1b3f']]`

## 命令位置別の参照

- [`00bd1afc`](#insn-00bd1afc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1b00`](#insn-00bd1b00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1b0c`](#insn-00bd1b0c) → `01126928`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1b10`](#insn-00bd1b10) → [`00bd1b30`](#insn-00bd1b30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1b1c`](#insn-00bd1b1c) → `002b9c8e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd1b24`](#insn-00bd1b24) → [`00c5af10`](../00c5a/00c5af10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af10` · 推定シンボル `None` · 推定型 `None`
- [`00bd1b2c`](#insn-00bd1b2c) → `01126928`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd1b30`](#insn-00bd1b30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1afc`](#insn-00bd1afc)

~~~json
{
  "source": "00bd1afc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1b00`](#insn-00bd1b00)

~~~json
{
  "source": "00bd1b00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1b0c`](#insn-00bd1b0c)

~~~json
{
  "source": "00bd1b0c",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1b10`](#insn-00bd1b10)

~~~json
{
  "source": "00bd1b10",
  "target": "00bd1b30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1b1c`](#insn-00bd1b1c)

~~~json
{
  "source": "00bd1b1c",
  "target": "002b9c8e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9c8a",
  "offset": 4,
  "size": 69,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002b9c8a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd1b24`](#insn-00bd1b24)

~~~json
{
  "source": "00bd1b24",
  "target": "00c5af10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1b2c`](#insn-00bd1b2c)

~~~json
{
  "source": "00bd1b2c",
  "target": "01126928",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126928",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd1b30`](#insn-00bd1b30)

~~~json
{
  "source": "00bd1b30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
