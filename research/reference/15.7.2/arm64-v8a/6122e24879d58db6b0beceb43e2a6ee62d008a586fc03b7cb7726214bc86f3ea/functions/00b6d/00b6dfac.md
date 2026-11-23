# 00b6dfac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b6e074`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b6e/00b6e074.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0073.md#compare-63cfbcaa0ce3526331e4df64da0eed3e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6dfac",
  "name": "_ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "25614b5a77c1835b443f0a8d391ec2f965933507ead2a3698fa1e918a2fdc74b",
  "source_text_sha256": "25614b5a77c1835b443f0a8d391ec2f965933507ead2a3698fa1e918a2fdc74b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6dfac",
        "00b6e01b"
      ]
    ],
    "bytes_sha256": "eb7e19b5cff181ae2c49f70240759ec279e2c1c54627d1b9d6080d67e5baef2e",
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

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 695 bytes

~~~c

void _ZN8firebase4auth8metadata14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a19f8 == 0) {
    DAT_010a19f8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseUserMetadata",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a19f8,&PTR_s_getLastSignInTimestamp_00c12960,2,&DAT_010a1a08,
             "com/google/firebase/auth/FirebaseUserMetadata");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6dfac"></a> `00b6dfac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b6dfb0"></a> `00b6dfb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6dfb4"></a> `00b6dfb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b6dfb8"></a> `00b6dfb8` | `b4 29 00 90` | adrp x20,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6dfbc"></a> `00b6dfbc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00b6dfc0"></a> `00b6dfc0` | `81 fe 44 f9` | ldr x1,[x20, #0x9f8] | `FALL_THROUGH`
<a id="insn-00b6dfc4"></a> `00b6dfc4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b6dfc8"></a> `00b6dfc8` | `41 01 00 b5` | cbnz x1,0x00b6dff0 | `CONDITIONAL_JUMP`
<a id="insn-00b6dfcc"></a> `00b6dfcc` | `03 ba ff 90` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00b6dfd0"></a> `00b6dfd0` | `63 40 19 91` | add x3,x3,#0x650 | `FALL_THROUGH`
<a id="insn-00b6dfd4"></a> `00b6dfd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6dfd8"></a> `00b6dfd8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00b6dfdc"></a> `00b6dfdc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00b6dfe0"></a> `00b6dfe0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00b6dfe4"></a> `00b6dfe4` | `eb bf 01 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00b6dfe8"></a> `00b6dfe8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00b6dfec"></a> `00b6dfec` | `80 fe 04 f9` | str x0,[x20, #0x9f8] | `FALL_THROUGH`
<a id="insn-00b6dff0"></a> `00b6dff0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6dff4"></a> `00b6dff4` | `22 05 00 b0` | adrp x2,0xc12000 | `FALL_THROUGH`
<a id="insn-00b6dff8"></a> `00b6dff8` | `a4 29 00 90` | adrp x4,0x10a1000 | `FALL_THROUGH`
<a id="insn-00b6dffc"></a> `00b6dffc` | `05 ba ff 90` | adrp x5,0x2ad000 | `FALL_THROUGH`
<a id="insn-00b6e000"></a> `00b6e000` | `42 80 25 91` | add x2,x2,#0x960 | `FALL_THROUGH`
<a id="insn-00b6e004"></a> `00b6e004` | `84 20 28 91` | add x4,x4,#0xa08 | `FALL_THROUGH`
<a id="insn-00b6e008"></a> `00b6e008` | `a5 40 19 91` | add x5,x5,#0x650 | `FALL_THROUGH`
<a id="insn-00b6e00c"></a> `00b6e00c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00b6e010"></a> `00b6e010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6e014"></a> `00b6e014` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6e018"></a> `00b6e018` | `e6 bf 01 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6dfac`](#insn-00b6dfac) 範囲 `[['00b6dfac', '00b6dfcb']]`
  - `CONDITIONAL_JUMP` [`00b6dfc8`](#insn-00b6dfc8) → [`00b6dff0`](#insn-00b6dff0)
  - `FALL_THROUGH` [`00b6dfc8`](#insn-00b6dfc8) → [`00b6dfcc`](#insn-00b6dfcc)
- ブロック [`00b6dfcc`](#insn-00b6dfcc) 範囲 `[['00b6dfcc', '00b6dfef']]`
  - `FALL_THROUGH` [`00b6dfec`](#insn-00b6dfec) → [`00b6dff0`](#insn-00b6dff0)
- ブロック [`00b6dff0`](#insn-00b6dff0) 範囲 `[['00b6dff0', '00b6e01b']]`

## 命令位置別の参照

- [`00b6dfac`](#insn-00b6dfac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dfb0`](#insn-00b6dfb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dfc0`](#insn-00b6dfc0) → `010a19f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6dfc8`](#insn-00b6dfc8) → [`00b6dff0`](#insn-00b6dff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dfd0`](#insn-00b6dfd0) → `002ad650`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6dfe4`](#insn-00b6dfe4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00b6dfec`](#insn-00b6dfec) → `010a19f8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6dff0`](#insn-00b6dff0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6e000`](#insn-00b6e000) → `00c12960`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b6e004`](#insn-00b6e004) → `010a1a08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b6e008`](#insn-00b6e008) → `002ad650`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6e018`](#insn-00b6e018) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6dfac`](#insn-00b6dfac)

~~~json
{
  "source": "00b6dfac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dfb0`](#insn-00b6dfb0)

~~~json
{
  "source": "00b6dfb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dfc0`](#insn-00b6dfc0)

~~~json
{
  "source": "00b6dfc0",
  "target": "010a19f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a19f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6dfc8`](#insn-00b6dfc8)

~~~json
{
  "source": "00b6dfc8",
  "target": "00b6dff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dfd0`](#insn-00b6dfd0)

~~~json
{
  "source": "00b6dfd0",
  "target": "002ad650",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad64c",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ad64c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b6dfe4`](#insn-00b6dfe4)

~~~json
{
  "source": "00b6dfe4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6dfec`](#insn-00b6dfec)

~~~json
{
  "source": "00b6dfec",
  "target": "010a19f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a19f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6dff0`](#insn-00b6dff0)

~~~json
{
  "source": "00b6dff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6e000`](#insn-00b6e000)

~~~json
{
  "source": "00b6e000",
  "target": "00c12960",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c12960",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b6e004`](#insn-00b6e004)

~~~json
{
  "source": "00b6e004",
  "target": "010a1a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a1a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b6e008`](#insn-00b6e008)

~~~json
{
  "source": "00b6e008",
  "target": "002ad650",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad64c",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ad64c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b6e018`](#insn-00b6e018)

~~~json
{
  "source": "00b6e018",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
