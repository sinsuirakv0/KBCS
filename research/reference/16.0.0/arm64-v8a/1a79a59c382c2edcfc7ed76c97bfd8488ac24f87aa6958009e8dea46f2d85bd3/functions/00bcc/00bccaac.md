# 00bccaac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5d5ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d5ac.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-c9ffc83cd070217d39c05442e1ade0dc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcced4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcc/00bcced4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-34bafbd4e25f16cae3d2f8358ec8872c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccaac",
  "name": "_ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5c549cd155bb6e870de0031ca56b28f72ca41427dd340d542d81b6b5ce2a3f7e",
  "source_text_sha256": "5c549cd155bb6e870de0031ca56b28f72ca41427dd340d542d81b6b5ce2a3f7e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccaac",
        "00bccb1b"
      ]
    ],
    "bytes_sha256": "321383e2c2e46b04cf0e08b82bd86233e798592c7cb358de547e5ddb4a26fac0",
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
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 843 bytes

~~~c

void _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126418 == 0) {
    DAT_01126418 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/auth/internal/cpp/JniIdTokenListener",0);
  }
                    /* try { // try from 00bccb04 to 00cccb1b has its CatchHandler @ 00bce700 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126418,&PTR_s_<init>_00c91780,2,&DAT_01126428,
             "com/google/firebase/auth/internal/cpp/JniIdTokenListener");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccaac"></a> `00bccaac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bccab0"></a> `00bccab0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccab4"></a> `00bccab4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bccab8"></a> `00bccab8` | `d4 2a 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccabc"></a> `00bccabc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bccac0"></a> `00bccac0` | `81 0e 42 f9` | ldr x1,[x20, #0x418] | `FALL_THROUGH`
<a id="insn-00bccac4"></a> `00bccac4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bccac8"></a> `00bccac8` | `41 01 00 b5` | cbnz x1,0x00bccaf0 | `CONDITIONAL_JUMP`
<a id="insn-00bccacc"></a> `00bccacc` | `e3 b6 ff d0` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bccad0"></a> `00bccad0` | `63 f4 22 91` | add x3,x3,#0x8bd | `FALL_THROUGH`
<a id="insn-00bccad4"></a> `00bccad4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccad8"></a> `00bccad8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bccadc"></a> `00bccadc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bccae0"></a> `00bccae0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bccae4"></a> `00bccae4` | `0b 38 02 94` | bl 0x00c5ab10 | `UNCONDITIONAL_CALL`
<a id="insn-00bccae8"></a> `00bccae8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bccaec"></a> `00bccaec` | `80 0e 02 f9` | str x0,[x20, #0x418] | `FALL_THROUGH`
<a id="insn-00bccaf0"></a> `00bccaf0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccaf4"></a> `00bccaf4` | `22 06 00 b0` | adrp x2,0xc91000 | `FALL_THROUGH`
<a id="insn-00bccaf8"></a> `00bccaf8` | `c4 2a 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bccafc"></a> `00bccafc` | `e5 b6 ff d0` | adrp x5,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bccb00"></a> `00bccb00` | `42 00 1e 91` | add x2,x2,#0x780 | `FALL_THROUGH`
<a id="insn-00bccb04"></a> `00bccb04` | `84 a0 10 91` | add x4,x4,#0x428 | `FALL_THROUGH`
<a id="insn-00bccb08"></a> `00bccb08` | `a5 f4 22 91` | add x5,x5,#0x8bd | `FALL_THROUGH`
<a id="insn-00bccb0c"></a> `00bccb0c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bccb10"></a> `00bccb10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bccb14"></a> `00bccb14` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bccb18"></a> `00bccb18` | `06 38 02 14` | b 0x00c5ab30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccaac`](#insn-00bccaac) 範囲 `[['00bccaac', '00bccacb']]`
  - `CONDITIONAL_JUMP` [`00bccac8`](#insn-00bccac8) → [`00bccaf0`](#insn-00bccaf0)
  - `FALL_THROUGH` [`00bccac8`](#insn-00bccac8) → [`00bccacc`](#insn-00bccacc)
- ブロック [`00bccacc`](#insn-00bccacc) 範囲 `[['00bccacc', '00bccaef']]`
  - `FALL_THROUGH` [`00bccaec`](#insn-00bccaec) → [`00bccaf0`](#insn-00bccaf0)
- ブロック [`00bccaf0`](#insn-00bccaf0) 範囲 `[['00bccaf0', '00bccb03']]`
  - `FALL_THROUGH` [`00bccb00`](#insn-00bccb00) → [`00bccb04`](#insn-00bccb04)
- ブロック [`00bccb04`](#insn-00bccb04) 範囲 `[['00bccb04', '00bccb1b']]`

## 命令位置別の参照

- [`00bccaac`](#insn-00bccaac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccab0`](#insn-00bccab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccac0`](#insn-00bccac0) → `01126418`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccac8`](#insn-00bccac8) → [`00bccaf0`](#insn-00bccaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccad0`](#insn-00bccad0) → `002aa8bd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccae4`](#insn-00bccae4) → [`00c5ab10`](../00c5a/00c5ab10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab10` · 推定シンボル `None` · 推定型 `None`
- [`00bccaec`](#insn-00bccaec) → `01126418`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccaf0`](#insn-00bccaf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccb00`](#insn-00bccb00) → `00c91780`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bccb04`](#insn-00bccb04) → `01126428`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bccb08`](#insn-00bccb08) → `002aa8bd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bccb18`](#insn-00bccb18) → [`00c5ab30`](../00c5a/00c5ab30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccaac`](#insn-00bccaac)

~~~json
{
  "source": "00bccaac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccab0`](#insn-00bccab0)

~~~json
{
  "source": "00bccab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccac0`](#insn-00bccac0)

~~~json
{
  "source": "00bccac0",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccac8`](#insn-00bccac8)

~~~json
{
  "source": "00bccac8",
  "target": "00bccaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccad0`](#insn-00bccad0)

~~~json
{
  "source": "00bccad0",
  "target": "002aa8bd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa8bd",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa8bd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccae4`](#insn-00bccae4)

~~~json
{
  "source": "00bccae4",
  "target": "00c5ab10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccaec`](#insn-00bccaec)

~~~json
{
  "source": "00bccaec",
  "target": "01126418",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126418",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccaf0`](#insn-00bccaf0)

~~~json
{
  "source": "00bccaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccb00`](#insn-00bccb00)

~~~json
{
  "source": "00bccb00",
  "target": "00c91780",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91780",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bccb04`](#insn-00bccb04)

~~~json
{
  "source": "00bccb04",
  "target": "01126428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126428",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bccb08`](#insn-00bccb08)

~~~json
{
  "source": "00bccb08",
  "target": "002aa8bd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa8bd",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa8bd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bccb18`](#insn-00bccb18)

~~~json
{
  "source": "00bccb18",
  "target": "00c5ab30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
