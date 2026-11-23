# 00ae0dfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae0ec4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ec4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-cc1646cabb4b709912b7ab570f92fa1d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae0dfc",
  "name": "_ZN8firebase9analytics24analytics_consent_status13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "48c951c547067a61feafd73071db8dbb74ceb4b16cbc8d48ef29b36bf60e7a65",
  "source_text_sha256": "48c951c547067a61feafd73071db8dbb74ceb4b16cbc8d48ef29b36bf60e7a65",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae0dfc",
        "00ae0e6b"
      ]
    ],
    "bytes_sha256": "7b6943bfc1f90a36a195cf869fdfdacf81102c45ca86bc6e2b56bbab67258f4b",
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

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 757 bytes

~~~c

void _ZN8firebase9analytics24analytics_consent_status13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0018 == 0) {
    DAT_010a0018 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,
                              "com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0018,&PTR_s_GRANTED_00c0fb20,2,&DAT_010a0030,
             "com/google/firebase/analytics/FirebaseAnalytics$ConsentStatus");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae0dfc"></a> `00ae0dfc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae0e00"></a> `00ae0e00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0e04"></a> `00ae0e04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae0e08"></a> `00ae0e08` | `14 2e 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae0e0c"></a> `00ae0e0c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ae0e10"></a> `00ae0e10` | `81 0e 40 f9` | ldr x1,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00ae0e14"></a> `00ae0e14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae0e18"></a> `00ae0e18` | `41 01 00 b5` | cbnz x1,0x00ae0e40 | `CONDITIONAL_JUMP`
<a id="insn-00ae0e1c"></a> `00ae0e1c` | `a3 bd ff 90` | adrp x3,0x294000 | `FALL_THROUGH`
<a id="insn-00ae0e20"></a> `00ae0e20` | `63 64 03 91` | add x3,x3,#0xd9 | `FALL_THROUGH`
<a id="insn-00ae0e24"></a> `00ae0e24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae0e28"></a> `00ae0e28` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00ae0e2c"></a> `00ae0e2c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae0e30"></a> `00ae0e30` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae0e34"></a> `00ae0e34` | `57 f4 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae0e38"></a> `00ae0e38` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ae0e3c"></a> `00ae0e3c` | `80 0e 00 f9` | str x0,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00ae0e40"></a> `00ae0e40` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae0e44"></a> `00ae0e44` | `62 09 00 f0` | adrp x2,0xc0f000 | `FALL_THROUGH`
<a id="insn-00ae0e48"></a> `00ae0e48` | `04 2e 00 90` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae0e4c"></a> `00ae0e4c` | `a5 bd ff 90` | adrp x5,0x294000 | `FALL_THROUGH`
<a id="insn-00ae0e50"></a> `00ae0e50` | `42 80 2c 91` | add x2,x2,#0xb20 | `FALL_THROUGH`
<a id="insn-00ae0e54"></a> `00ae0e54` | `84 c0 00 91` | add x4,x4,#0x30 | `FALL_THROUGH`
<a id="insn-00ae0e58"></a> `00ae0e58` | `a5 64 03 91` | add x5,x5,#0xd9 | `FALL_THROUGH`
<a id="insn-00ae0e5c"></a> `00ae0e5c` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00ae0e60"></a> `00ae0e60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae0e64"></a> `00ae0e64` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae0e68"></a> `00ae0e68` | `42 f4 03 14` | b 0x00bddf70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae0dfc`](#insn-00ae0dfc) 範囲 `[['00ae0dfc', '00ae0e1b']]`
  - `CONDITIONAL_JUMP` [`00ae0e18`](#insn-00ae0e18) → [`00ae0e40`](#insn-00ae0e40)
  - `FALL_THROUGH` [`00ae0e18`](#insn-00ae0e18) → [`00ae0e1c`](#insn-00ae0e1c)
- ブロック [`00ae0e1c`](#insn-00ae0e1c) 範囲 `[['00ae0e1c', '00ae0e3f']]`
  - `FALL_THROUGH` [`00ae0e3c`](#insn-00ae0e3c) → [`00ae0e40`](#insn-00ae0e40)
- ブロック [`00ae0e40`](#insn-00ae0e40) 範囲 `[['00ae0e40', '00ae0e6b']]`

## 命令位置別の参照

- [`00ae0dfc`](#insn-00ae0dfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e00`](#insn-00ae0e00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e10`](#insn-00ae0e10) → `010a0018`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0e18`](#insn-00ae0e18) → [`00ae0e40`](#insn-00ae0e40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e20`](#insn-00ae0e20) → `002940d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae0e34`](#insn-00ae0e34) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e3c`](#insn-00ae0e3c) → `010a0018`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0e40`](#insn-00ae0e40) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae0e50`](#insn-00ae0e50) → `00c0fb20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ae0e54`](#insn-00ae0e54) → `010a0030`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae0e58`](#insn-00ae0e58) → `002940d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae0e68`](#insn-00ae0e68) → [`00bddf70`](../00bdd/00bddf70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae0dfc`](#insn-00ae0dfc)

~~~json
{
  "source": "00ae0dfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e00`](#insn-00ae0e00)

~~~json
{
  "source": "00ae0e00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e10`](#insn-00ae0e10)

~~~json
{
  "source": "00ae0e10",
  "target": "010a0018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0e18`](#insn-00ae0e18)

~~~json
{
  "source": "00ae0e18",
  "target": "00ae0e40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e20`](#insn-00ae0e20)

~~~json
{
  "source": "00ae0e20",
  "target": "002940d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002940d5",
  "offset": 4,
  "size": 66,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f616e616c79746963",
  "capture_start": "002940d5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae0e34`](#insn-00ae0e34)

~~~json
{
  "source": "00ae0e34",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae0e3c`](#insn-00ae0e3c)

~~~json
{
  "source": "00ae0e3c",
  "target": "010a0018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0018",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0e40`](#insn-00ae0e40)

~~~json
{
  "source": "00ae0e40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae0e50`](#insn-00ae0e50)

~~~json
{
  "source": "00ae0e50",
  "target": "00c0fb20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0fb20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ae0e54`](#insn-00ae0e54)

~~~json
{
  "source": "00ae0e54",
  "target": "010a0030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0030",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae0e58`](#insn-00ae0e58)

~~~json
{
  "source": "00ae0e58",
  "target": "002940d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002940d5",
  "offset": 4,
  "size": 66,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f616e616c79746963",
  "capture_start": "002940d5",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ae0e68`](#insn-00ae0e68)

~~~json
{
  "source": "00ae0e68",
  "target": "00bddf70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
