# 00bdcbe0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b6d6e0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b6d/00b6d6e0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0070.md#compare-0ca373a9a8c98565f8f61f292dd02a5a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdd008`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdd008.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0085.md#compare-b6a707d822b8f94b4c562756f77bd1b0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbe0",
  "name": "_ZN8firebase4auth11tokenresult14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea6352b68d307cca8658d84a697a10b230334989b5db4b12fe2645c13fd699d0",
  "source_text_sha256": "ea6352b68d307cca8658d84a697a10b230334989b5db4b12fe2645c13fd699d0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbe0",
        "00bdcc4f"
      ]
    ],
    "bytes_sha256": "a76998c26bc6ae04dc3828fde74571fc05ba8c564e5aa4abf970703399538089",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5ab10](../00c5a/00c5ab10.md)
- [00c5ab30](../00c5a/00c5ab30.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/GetTokenResult"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 673 bytes

~~~c

void _ZN8firebase4auth11tokenresult14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126900 == 0) {
    DAT_01126900 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GetTokenResult",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126900,&PTR_s_getToken_00c921e0,1,&DAT_01126910,
             "com/google/firebase/auth/GetTokenResult");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbe0"></a> `00bdcbe0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdcbe4"></a> `00bdcbe4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcbe8"></a> `00bdcbe8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcbec"></a> `00bdcbec` | `54 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcbf0"></a> `00bdcbf0` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bdcbf4"></a> `00bdcbf4` | `81 82 44 f9` | ldr x1,[x20, #0x900] | `FALL_THROUGH`
<a id="insn-00bdcbf8"></a> `00bdcbf8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdcbfc"></a> `00bdcbfc` | `41 01 00 b5` | cbnz x1,0x00bdcc24 | `CONDITIONAL_JUMP`
<a id="insn-00bdcc00"></a> `00bdcc00` | `03 b7 ff 90` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bdcc04"></a> `00bdcc04` | `63 40 08 91` | add x3,x3,#0x210 | `FALL_THROUGH`
<a id="insn-00bdcc08"></a> `00bdcc08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcc0c"></a> `00bdcc0c` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bdcc10"></a> `00bdcc10` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bdcc14"></a> `00bdcc14` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bdcc18"></a> `00bdcc18` | `be f7 01 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcc1c"></a> `00bdcc1c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bdcc20"></a> `00bdcc20` | `80 82 04 f9` | str x0,[x20, #0x900] | `FALL_THROUGH`
<a id="insn-00bdcc24"></a> `00bdcc24` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcc28"></a> `00bdcc28` | `a2 05 00 d0` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bdcc2c"></a> `00bdcc2c` | `44 2a 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdcc30"></a> `00bdcc30` | `05 b7 ff 90` | adrp x5,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bdcc34"></a> `00bdcc34` | `42 80 07 91` | add x2,x2,#0x1e0 | `FALL_THROUGH`
<a id="insn-00bdcc38"></a> `00bdcc38` | `84 40 24 91` | add x4,x4,#0x910 | `FALL_THROUGH`
<a id="insn-00bdcc3c"></a> `00bdcc3c` | `a5 40 08 91` | add x5,x5,#0x210 | `FALL_THROUGH`
<a id="insn-00bdcc40"></a> `00bdcc40` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bdcc44"></a> `00bdcc44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcc48"></a> `00bdcc48` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdcc4c"></a> `00bdcc4c` | `b9 f7 01 14` | b 0x00c5ab30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbe0`](#insn-00bdcbe0) 範囲 `[['00bdcbe0', '00bdcbff']]`
  - `CONDITIONAL_JUMP` [`00bdcbfc`](#insn-00bdcbfc) → [`00bdcc24`](#insn-00bdcc24)
  - `FALL_THROUGH` [`00bdcbfc`](#insn-00bdcbfc) → [`00bdcc00`](#insn-00bdcc00)
- ブロック [`00bdcc00`](#insn-00bdcc00) 範囲 `[['00bdcc00', '00bdcc23']]`
  - `FALL_THROUGH` [`00bdcc20`](#insn-00bdcc20) → [`00bdcc24`](#insn-00bdcc24)
- ブロック [`00bdcc24`](#insn-00bdcc24) 範囲 `[['00bdcc24', '00bdcc4f']]`

## 命令位置別の参照

- [`00bdcbe0`](#insn-00bdcbe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbe4`](#insn-00bdcbe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbf4`](#insn-00bdcbf4) → `01126900`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcbfc`](#insn-00bdcbfc) → [`00bdcc24`](#insn-00bdcc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc04`](#insn-00bdcc04) → `002bc210`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdcc18`](#insn-00bdcc18) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc20`](#insn-00bdcc20) → `01126900`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcc24`](#insn-00bdcc24) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc34`](#insn-00bdcc34) → `00c921e0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcc38`](#insn-00bdcc38) → `01126910`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcc3c`](#insn-00bdcc3c) → `002bc210`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdcc4c`](#insn-00bdcc4c) → [`00c5ab30`](../00c5a/00c5ab30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbe0`](#insn-00bdcbe0)

~~~json
{
  "source": "00bdcbe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbe4`](#insn-00bdcbe4)

~~~json
{
  "source": "00bdcbe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbf4`](#insn-00bdcbf4)

~~~json
{
  "source": "00bdcbf4",
  "target": "01126900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126900",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcbfc`](#insn-00bdcbfc)

~~~json
{
  "source": "00bdcbfc",
  "target": "00bdcc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc04`](#insn-00bdcc04)

~~~json
{
  "source": "00bdcc04",
  "target": "002bc210",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc20c",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc20c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdcc18`](#insn-00bdcc18)

~~~json
{
  "source": "00bdcc18",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcc20`](#insn-00bdcc20)

~~~json
{
  "source": "00bdcc20",
  "target": "01126900",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126900",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcc24`](#insn-00bdcc24)

~~~json
{
  "source": "00bdcc24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc34`](#insn-00bdcc34)

~~~json
{
  "source": "00bdcc34",
  "target": "00c921e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c921e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcc38`](#insn-00bdcc38)

~~~json
{
  "source": "00bdcc38",
  "target": "01126910",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126910",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcc3c`](#insn-00bdcc3c)

~~~json
{
  "source": "00bdcc3c",
  "target": "002bc210",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc20c",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc20c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdcc4c`](#insn-00bdcc4c)

~~~json
{
  "source": "00bdcc4c",
  "target": "00c5ab30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
