# 00bd7efc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd7e60`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd7/00bd7e60.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0084.md#compare-2cd35a9b74a8595667bb8c91dcf3c5c2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd8ef0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd8/00bd8ef0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-8f0f699270bad34043033aef0d0d30ea)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd7efc",
  "name": "_ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5732cdf6db028b8788506c593a25af6108ced58ba12838d7c1cf0f95695311f4",
  "source_text_sha256": "5732cdf6db028b8788506c593a25af6108ced58ba12838d7c1cf0f95695311f4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd7efc",
        "00bd7f6b"
      ]
    ],
    "bytes_sha256": "7b24fa64c314f601065c79640ff53c3bf671bbea5e851763500401de98f2227c",
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
"%PG%com/google/firebase/auth/FirebaseUser"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 689 bytes

~~~c

void _ZN8firebase4auth8user_idp14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_01126d88 == 0) {
    DAT_01126d88 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUser",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_01126d88,&PTR_s_startActivityForLinkWithProvider_00c92528,2,&DAT_01126d98,
             "com/google/firebase/auth/FirebaseUser");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd7efc"></a> `00bd7efc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd7f00"></a> `00bd7f00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7f04"></a> `00bd7f04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd7f08"></a> `00bd7f08` | `74 2a 00 f0` | adrp x20,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd7f0c"></a> `00bd7f0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00bd7f10"></a> `00bd7f10` | `81 c6 46 f9` | ldr x1,[x20, #0xd88] | `FALL_THROUGH`
<a id="insn-00bd7f14"></a> `00bd7f14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd7f18"></a> `00bd7f18` | `41 01 00 b5` | cbnz x1,0x00bd7f40 | `CONDITIONAL_JUMP`
<a id="insn-00bd7f1c"></a> `00bd7f1c` | `83 b6 ff d0` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bd7f20"></a> `00bd7f20` | `63 d8 22 91` | add x3,x3,#0x8b6 | `FALL_THROUGH`
<a id="insn-00bd7f24"></a> `00bd7f24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd7f28"></a> `00bd7f28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bd7f2c"></a> `00bd7f2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bd7f30"></a> `00bd7f30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bd7f34"></a> `00bd7f34` | `2b 0c 02 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd7f38"></a> `00bd7f38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bd7f3c"></a> `00bd7f3c` | `80 c6 06 f9` | str x0,[x20, #0xd88] | `FALL_THROUGH`
<a id="insn-00bd7f40"></a> `00bd7f40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd7f44"></a> `00bd7f44` | `c2 05 00 f0` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bd7f48"></a> `00bd7f48` | `64 2a 00 f0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd7f4c"></a> `00bd7f4c` | `85 b6 ff d0` | adrp x5,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bd7f50"></a> `00bd7f50` | `42 a0 14 91` | add x2,x2,#0x528 | `FALL_THROUGH`
<a id="insn-00bd7f54"></a> `00bd7f54` | `84 60 36 91` | add x4,x4,#0xd98 | `FALL_THROUGH`
<a id="insn-00bd7f58"></a> `00bd7f58` | `a5 d8 22 91` | add x5,x5,#0x8b6 | `FALL_THROUGH`
<a id="insn-00bd7f5c"></a> `00bd7f5c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bd7f60"></a> `00bd7f60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd7f64"></a> `00bd7f64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd7f68"></a> `00bd7f68` | `26 0c 02 14` | b 0x00c5b000 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd7efc`](#insn-00bd7efc) 範囲 `[['00bd7efc', '00bd7f1b']]`
  - `CONDITIONAL_JUMP` [`00bd7f18`](#insn-00bd7f18) → [`00bd7f40`](#insn-00bd7f40)
  - `FALL_THROUGH` [`00bd7f18`](#insn-00bd7f18) → [`00bd7f1c`](#insn-00bd7f1c)
- ブロック [`00bd7f1c`](#insn-00bd7f1c) 範囲 `[['00bd7f1c', '00bd7f3f']]`
  - `FALL_THROUGH` [`00bd7f3c`](#insn-00bd7f3c) → [`00bd7f40`](#insn-00bd7f40)
- ブロック [`00bd7f40`](#insn-00bd7f40) 範囲 `[['00bd7f40', '00bd7f6b']]`

## 命令位置別の参照

- [`00bd7efc`](#insn-00bd7efc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7f00`](#insn-00bd7f00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7f10`](#insn-00bd7f10) → `01126d88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd7f18`](#insn-00bd7f18) → [`00bd7f40`](#insn-00bd7f40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7f20`](#insn-00bd7f20) → `002a98b6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd7f34`](#insn-00bd7f34) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bd7f3c`](#insn-00bd7f3c) → `01126d88`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd7f40`](#insn-00bd7f40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd7f50`](#insn-00bd7f50) → `00c92528`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bd7f54`](#insn-00bd7f54) → `01126d98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd7f58`](#insn-00bd7f58) → `002a98b6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd7f68`](#insn-00bd7f68) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd7efc`](#insn-00bd7efc)

~~~json
{
  "source": "00bd7efc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7f00`](#insn-00bd7f00)

~~~json
{
  "source": "00bd7f00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7f10`](#insn-00bd7f10)

~~~json
{
  "source": "00bd7f10",
  "target": "01126d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7f18`](#insn-00bd7f18)

~~~json
{
  "source": "00bd7f18",
  "target": "00bd7f40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7f20`](#insn-00bd7f20)

~~~json
{
  "source": "00bd7f20",
  "target": "002a98b6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a98b2",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a98b2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd7f34`](#insn-00bd7f34)

~~~json
{
  "source": "00bd7f34",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd7f3c`](#insn-00bd7f3c)

~~~json
{
  "source": "00bd7f3c",
  "target": "01126d88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7f40`](#insn-00bd7f40)

~~~json
{
  "source": "00bd7f40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd7f50`](#insn-00bd7f50)

~~~json
{
  "source": "00bd7f50",
  "target": "00c92528",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92528",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd7f54`](#insn-00bd7f54)

~~~json
{
  "source": "00bd7f54",
  "target": "01126d98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd7f58`](#insn-00bd7f58)

~~~json
{
  "source": "00bd7f58",
  "target": "002a98b6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a98b2",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a98b2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bd7f68`](#insn-00bd7f68)

~~~json
{
  "source": "00bd7f68",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
