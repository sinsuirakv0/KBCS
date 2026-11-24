# 00b5cdac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5cd68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0070.md#compare-49003add0027c9a3c851107cadb78655)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcc2ac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcc/00bcc2ac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-e12c56503cc2c1a062e41ef365a33724)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5cdac",
  "name": "_ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a8d0758722b284965fb843cddb73ad2fec3b84d6ca6f34ebe23c25e35015bead",
  "source_text_sha256": "a8d0758722b284965fb843cddb73ad2fec3b84d6ca6f34ebe23c25e35015bead",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5cdac",
        "00b5cdef"
      ]
    ],
    "bytes_sha256": "8cafafde07fd3b7e2edb5c2af98f9438518968a12310738497d8ead47667b7c2",
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

- [00bde090](../00bde/00bde090.md)

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
  if (DAT_010a14c8 == 0) {
    DAT_010a14c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/SignInMethodQueryResult",
                              param_3);
  }
  return DAT_010a14c8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5cdac"></a> `00b5cdac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b5cdb0"></a> `00b5cdb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cdb4"></a> `00b5cdb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b5cdb8"></a> `00b5cdb8` | `33 2a 00 b0` | adrp x19,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b5cdbc"></a> `00b5cdbc` | `68 66 42 f9` | ldr x8,[x19, #0x4c8] | `FALL_THROUGH`
<a id="insn-00b5cdc0"></a> `00b5cdc0` | `08 01 00 b5` | cbnz x8,0x00b5cde0 | `CONDITIONAL_JUMP`
<a id="insn-00b5cdc4"></a> `00b5cdc4` | `a3 b9 ff f0` | adrp x3,0x293000 | `FALL_THROUGH`
<a id="insn-00b5cdc8"></a> `00b5cdc8` | `e4 03 02 2a` | mov w4,w2 | `FALL_THROUGH`
<a id="insn-00b5cdcc"></a> `00b5cdcc` | `63 38 10 91` | add x3,x3,#0x40e | `FALL_THROUGH`
<a id="insn-00b5cdd0"></a> `00b5cdd0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b5cdd4"></a> `00b5cdd4` | `af 04 02 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cdd8"></a> `00b5cdd8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00b5cddc"></a> `00b5cddc` | `60 66 02 f9` | str x0,[x19, #0x4c8] | `FALL_THROUGH`
<a id="insn-00b5cde0"></a> `00b5cde0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cde4"></a> `00b5cde4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00b5cde8"></a> `00b5cde8` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b5cdec"></a> `00b5cdec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5cdac`](#insn-00b5cdac) 範囲 `[['00b5cdac', '00b5cdc3']]`
  - `CONDITIONAL_JUMP` [`00b5cdc0`](#insn-00b5cdc0) → [`00b5cde0`](#insn-00b5cde0)
  - `FALL_THROUGH` [`00b5cdc0`](#insn-00b5cdc0) → [`00b5cdc4`](#insn-00b5cdc4)
- ブロック [`00b5cdc4`](#insn-00b5cdc4) 範囲 `[['00b5cdc4', '00b5cddf']]`
  - `FALL_THROUGH` [`00b5cddc`](#insn-00b5cddc) → [`00b5cde0`](#insn-00b5cde0)
- ブロック [`00b5cde0`](#insn-00b5cde0) 範囲 `[['00b5cde0', '00b5cdef']]`

## 命令位置別の参照

- [`00b5cdac`](#insn-00b5cdac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cdb0`](#insn-00b5cdb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cdbc`](#insn-00b5cdbc) → `010a14c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5cdc0`](#insn-00b5cdc0) → [`00b5cde0`](#insn-00b5cde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cdcc`](#insn-00b5cdcc) → `0029340e`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b5cdd4`](#insn-00b5cdd4) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00b5cddc`](#insn-00b5cddc) → `010a14c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5cde0`](#insn-00b5cde0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5cdac`](#insn-00b5cdac)

~~~json
{
  "source": "00b5cdac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cdb0`](#insn-00b5cdb0)

~~~json
{
  "source": "00b5cdb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cdbc`](#insn-00b5cdbc)

~~~json
{
  "source": "00b5cdbc",
  "target": "010a14c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cdc0`](#insn-00b5cdc0)

~~~json
{
  "source": "00b5cdc0",
  "target": "00b5cde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cdcc`](#insn-00b5cdcc)

~~~json
{
  "source": "00b5cdcc",
  "target": "0029340e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029340a",
  "offset": 4,
  "size": 53,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f536967",
  "capture_start": "0029340a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b5cdd4`](#insn-00b5cdd4)

~~~json
{
  "source": "00b5cdd4",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cddc`](#insn-00b5cddc)

~~~json
{
  "source": "00b5cddc",
  "target": "010a14c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a14c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cde0`](#insn-00b5cde0)

~~~json
{
  "source": "00b5cde0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
