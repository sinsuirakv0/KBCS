# 00bcc2ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5cdac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-e12c56503cc2c1a062e41ef365a33724)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcc6d4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcc6d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-d74b7059076d959bee03ba395b50581c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcc2ac",
  "name": "_ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2c3ddfb6c8e555ac83367a8ba485c390cd894f7e6de27013fb200b8b8975f958",
  "source_text_sha256": "2c3ddfb6c8e555ac83367a8ba485c390cd894f7e6de27013fb200b8b8975f958",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcc2ac",
        "00bcc2ef"
      ]
    ],
    "bytes_sha256": "cec1aeba1450f89dfb0090603ce15c7b6512a66db848d5622ba64c1a720a7490",
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

- [00c5ab10](../00c5a/00c5ab10.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/SignInMethodQueryResult"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 545 bytes

~~~c

long _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE
               (undefined8 param_1,undefined8 param_2,undefined4 param_3)

{
  if (DAT_011263d0 == 0) {
    DAT_011263d0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/SignInMethodQueryResult",
                              param_3);
  }
  return DAT_011263d0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcc2ac"></a> `00bcc2ac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcc2b0"></a> `00bcc2b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc2b4"></a> `00bcc2b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcc2b8"></a> `00bcc2b8` | `d3 2a 00 d0` | adrp x19,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcc2bc"></a> `00bcc2bc` | `68 ea 41 f9` | ldr x8,[x19, #0x3d0] | `FALL_THROUGH`
<a id="insn-00bcc2c0"></a> `00bcc2c0` | `08 01 00 b5` | cbnz x8,0x00bcc2e0 | `CONDITIONAL_JUMP`
<a id="insn-00bcc2c4"></a> `00bcc2c4` | `a3 b6 ff d0` | adrp x3,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bcc2c8"></a> `00bcc2c8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00bcc2cc"></a> `00bcc2cc` | `63 d4 2f 91` | add x3,x3,#0xbf5 | `FALL_THROUGH`
<a id="insn-00bcc2d0"></a> `00bcc2d0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bcc2d4"></a> `00bcc2d4` | `0f 3a 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc2d8"></a> `00bcc2d8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcc2dc"></a> `00bcc2dc` | `60 ea 01 f9` | str x0,[x19, #0x3d0] | `FALL_THROUGH`
<a id="insn-00bcc2e0"></a> `00bcc2e0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc2e4"></a> `00bcc2e4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcc2e8"></a> `00bcc2e8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcc2ec"></a> `00bcc2ec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcc2ac`](#insn-00bcc2ac) 範囲 `[['00bcc2ac', '00bcc2c3']]`
  - `CONDITIONAL_JUMP` [`00bcc2c0`](#insn-00bcc2c0) → [`00bcc2e0`](#insn-00bcc2e0)
  - `FALL_THROUGH` [`00bcc2c0`](#insn-00bcc2c0) → [`00bcc2c4`](#insn-00bcc2c4)
- ブロック [`00bcc2c4`](#insn-00bcc2c4) 範囲 `[['00bcc2c4', '00bcc2df']]`
  - `FALL_THROUGH` [`00bcc2dc`](#insn-00bcc2dc) → [`00bcc2e0`](#insn-00bcc2e0)
- ブロック [`00bcc2e0`](#insn-00bcc2e0) 範囲 `[['00bcc2e0', '00bcc2ef']]`

## 命令位置別の参照

- [`00bcc2ac`](#insn-00bcc2ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc2b0`](#insn-00bcc2b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc2bc`](#insn-00bcc2bc) → `011263d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc2c0`](#insn-00bcc2c0) → [`00bcc2e0`](#insn-00bcc2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc2cc`](#insn-00bcc2cc) → `002a2bf5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcc2d4`](#insn-00bcc2d4) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bcc2dc`](#insn-00bcc2dc) → `011263d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcc2e0`](#insn-00bcc2e0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcc2ac`](#insn-00bcc2ac)

~~~json
{
  "source": "00bcc2ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc2b0`](#insn-00bcc2b0)

~~~json
{
  "source": "00bcc2b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc2bc`](#insn-00bcc2bc)

~~~json
{
  "source": "00bcc2bc",
  "target": "011263d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc2c0`](#insn-00bcc2c0)

~~~json
{
  "source": "00bcc2c0",
  "target": "00bcc2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc2cc`](#insn-00bcc2cc)

~~~json
{
  "source": "00bcc2cc",
  "target": "002a2bf5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2bf1",
  "offset": 4,
  "size": 53,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f536967",
  "capture_start": "002a2bf1",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcc2d4`](#insn-00bcc2d4)

~~~json
{
  "source": "00bcc2d4",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc2dc`](#insn-00bcc2dc)

~~~json
{
  "source": "00bcc2dc",
  "target": "011263d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcc2e0`](#insn-00bcc2e0)

~~~json
{
  "source": "00bcc2e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
