# 00bb8eec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb8e50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb8/00bb8e50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-d35b0fbeade6f4c662a71aee1c4e3abc)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bb9ee0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bb9/00bb9ee0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0079.md#compare-dc758abdfbb0e817169688005616c0ca)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb8eec",
  "name": "_ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aae575e987bdd6dd3b631535da33bfbc8fbfc8744b83e4ac1a9c6ca11c7264f7",
  "source_text_sha256": "aae575e987bdd6dd3b631535da33bfbc8fbfc8744b83e4ac1a9c6ca11c7264f7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb8eec",
        "00bb8f5b"
      ]
    ],
    "bytes_sha256": "28eab552d333ae6821d828379151737c38e96c4ea396c95063981aa3363bdf7b",
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

- [00c5afe0](../00c5a/00c5afe0.md)
- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/messaging/FirebaseMessaging"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 814 bytes

~~~c

void _ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_011263a8 == 0) {
    DAT_011263a8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/messaging/FirebaseMessaging",0)
    ;
  }
                    /* try { // try from 00bb8f54 to 00cb8f67 has its CatchHandler @ 00bb90f0 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_011263a8,&PTR_s_isAutoInitEnabled_00c91390,0xb,&DAT_011263b8,
             "com/google/firebase/messaging/FirebaseMessaging");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb8eec"></a> `00bb8eec` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bb8ef0"></a> `00bb8ef0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8ef4"></a> `00bb8ef4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bb8ef8"></a> `00bb8ef8` | `74 2b 00 d0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bb8efc"></a> `00bb8efc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bb8f00"></a> `00bb8f00` | `81 d6 41 f9` | ldr x1,[x20, #0x3a8] | `FALL_THROUGH`
<a id="insn-00bb8f04"></a> `00bb8f04` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb8f08"></a> `00bb8f08` | `41 01 00 b5` | cbnz x1,0x00bb8f30 | `CONDITIONAL_JUMP`
<a id="insn-00bb8f0c"></a> `00bb8f0c` | `03 b8 ff d0` | adrp x3,0x2ba000 | `FALL_THROUGH`
<a id="insn-00bb8f10"></a> `00bb8f10` | `63 28 39 91` | add x3,x3,#0xe4a | `FALL_THROUGH`
<a id="insn-00bb8f14"></a> `00bb8f14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb8f18"></a> `00bb8f18` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bb8f1c"></a> `00bb8f1c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bb8f20"></a> `00bb8f20` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bb8f24"></a> `00bb8f24` | `2f 88 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb8f28"></a> `00bb8f28` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bb8f2c"></a> `00bb8f2c` | `80 d6 01 f9` | str x0,[x20, #0x3a8] | `FALL_THROUGH`
<a id="insn-00bb8f30"></a> `00bb8f30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb8f34"></a> `00bb8f34` | `c2 06 00 b0` | adrp x2,0xc91000 | `FALL_THROUGH`
<a id="insn-00bb8f38"></a> `00bb8f38` | `64 2b 00 d0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bb8f3c"></a> `00bb8f3c` | `05 b8 ff d0` | adrp x5,0x2ba000 | `FALL_THROUGH`
<a id="insn-00bb8f40"></a> `00bb8f40` | `42 40 0e 91` | add x2,x2,#0x390 | `FALL_THROUGH`
<a id="insn-00bb8f44"></a> `00bb8f44` | `84 e0 0e 91` | add x4,x4,#0x3b8 | `FALL_THROUGH`
<a id="insn-00bb8f48"></a> `00bb8f48` | `a5 28 39 91` | add x5,x5,#0xe4a | `FALL_THROUGH`
<a id="insn-00bb8f4c"></a> `00bb8f4c` | `63 01 80 52` | mov w3,#0xb | `FALL_THROUGH`
<a id="insn-00bb8f50"></a> `00bb8f50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb8f54"></a> `00bb8f54` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bb8f58"></a> `00bb8f58` | `2a 88 02 14` | b 0x00c5b000 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb8eec`](#insn-00bb8eec) 範囲 `[['00bb8eec', '00bb8f0b']]`
  - `CONDITIONAL_JUMP` [`00bb8f08`](#insn-00bb8f08) → [`00bb8f30`](#insn-00bb8f30)
  - `FALL_THROUGH` [`00bb8f08`](#insn-00bb8f08) → [`00bb8f0c`](#insn-00bb8f0c)
- ブロック [`00bb8f0c`](#insn-00bb8f0c) 範囲 `[['00bb8f0c', '00bb8f2f']]`
  - `FALL_THROUGH` [`00bb8f2c`](#insn-00bb8f2c) → [`00bb8f30`](#insn-00bb8f30)
- ブロック [`00bb8f30`](#insn-00bb8f30) 範囲 `[['00bb8f30', '00bb8f53']]`
  - `FALL_THROUGH` [`00bb8f50`](#insn-00bb8f50) → [`00bb8f54`](#insn-00bb8f54)
- ブロック [`00bb8f54`](#insn-00bb8f54) 範囲 `[['00bb8f54', '00bb8f5b']]`

## 命令位置別の参照

- [`00bb8eec`](#insn-00bb8eec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8ef0`](#insn-00bb8ef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f00`](#insn-00bb8f00) → `011263a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8f08`](#insn-00bb8f08) → [`00bb8f30`](#insn-00bb8f30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f10`](#insn-00bb8f10) → `002bae4a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bb8f24`](#insn-00bb8f24) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f2c`](#insn-00bb8f2c) → `011263a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8f30`](#insn-00bb8f30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb8f40`](#insn-00bb8f40) → `00c91390`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bb8f44`](#insn-00bb8f44) → `011263b8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb8f48`](#insn-00bb8f48) → `002bae4a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bb8f58`](#insn-00bb8f58) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb8eec`](#insn-00bb8eec)

~~~json
{
  "source": "00bb8eec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8ef0`](#insn-00bb8ef0)

~~~json
{
  "source": "00bb8ef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f00`](#insn-00bb8f00)

~~~json
{
  "source": "00bb8f00",
  "target": "011263a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8f08`](#insn-00bb8f08)

~~~json
{
  "source": "00bb8f08",
  "target": "00bb8f30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f10`](#insn-00bb8f10)

~~~json
{
  "source": "00bb8f10",
  "target": "002bae4a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bae46",
  "offset": 4,
  "size": 52,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002bae46",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb8f24`](#insn-00bb8f24)

~~~json
{
  "source": "00bb8f24",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb8f2c`](#insn-00bb8f2c)

~~~json
{
  "source": "00bb8f2c",
  "target": "011263a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8f30`](#insn-00bb8f30)

~~~json
{
  "source": "00bb8f30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb8f40`](#insn-00bb8f40)

~~~json
{
  "source": "00bb8f40",
  "target": "00c91390",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91390",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bb8f44`](#insn-00bb8f44)

~~~json
{
  "source": "00bb8f44",
  "target": "011263b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263b8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bb8f48`](#insn-00bb8f48)

~~~json
{
  "source": "00bb8f48",
  "target": "002bae4a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bae46",
  "offset": 4,
  "size": 52,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f6d6573736167696e",
  "capture_start": "002bae46",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bb8f58`](#insn-00bb8f58)

~~~json
{
  "source": "00bb8f58",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
