# 00aece4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecf14`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-5cda75b8b4252add1c98e2c0f7811580)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aece4c",
  "name": "_ZN8firebase4util3set12ReleaseClassEP7_JNIEnv",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e3c2b111306abac3579ba31060d465a058733072c09b05cb6cf452d92d5818b",
  "source_text_sha256": "7e3c2b111306abac3579ba31060d465a058733072c09b05cb6cf452d92d5818b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aece4c",
        "00aeceeb"
      ]
    ],
    "bytes_sha256": "7366cb5c9fd72613b479a47352bd898f667af421ea9819ae77274efc3c350362",
    "instruction_count": 40,
    "instruction_bytes": 160,
    "body_bytes": 160,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 503 bytes

~~~c

void _ZN8firebase4util3set12ReleaseClassEP7_JNIEnv(long *param_1)

{
  char cVar1;
  
  if (DAT_010a08c8 != 0) {
    if (DAT_010a08d0 != '\0') {
      (**(code **)(*param_1 + 0x6c0))(param_1);
      DAT_010a08d0 = '\0';
    }
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    (**(code **)(*param_1 + 0xb0))(param_1,DAT_010a08c8);
    DAT_010a08c8 = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aece4c"></a> `00aece4c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aece50"></a> `00aece50` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aece54"></a> `00aece54` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aece58"></a> `00aece58` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aece5c"></a> `00aece5c` | `b4 2d 00 90` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aece60"></a> `00aece60` | `81 66 44 f9` | ldr x1,[x20, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aece64"></a> `00aece64` | `c1 03 00 b4` | cbz x1,0x00aecedc | `CONDITIONAL_JUMP`
<a id="insn-00aece68"></a> `00aece68` | `b5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aece6c"></a> `00aece6c` | `a8 42 63 39` | ldrb w8,[x21, #0x8d0] | `FALL_THROUGH`
<a id="insn-00aece70"></a> `00aece70` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aece74"></a> `00aece74` | `c8 00 00 34` | cbz w8,0x00aece8c | `CONDITIONAL_JUMP`
<a id="insn-00aece78"></a> `00aece78` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aece7c"></a> `00aece7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aece80"></a> `00aece80` | `08 61 43 f9` | ldr x8,[x8, #0x6c0] | `FALL_THROUGH`
<a id="insn-00aece84"></a> `00aece84` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aece88"></a> `00aece88` | `bf 42 23 39` | strb wzr,[x21, #0x8d0] | `FALL_THROUGH`
<a id="insn-00aece8c"></a> `00aece8c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aece90"></a> `00aece90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aece94"></a> `00aece94` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aece98"></a> `00aece98` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aece9c"></a> `00aece9c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aecea0"></a> `00aecea0` | `20 01 00 54` | b.eq 0x00aecec4 | `CONDITIONAL_JUMP`
<a id="insn-00aecea4"></a> `00aecea4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecea8"></a> `00aecea8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeceac"></a> `00aeceac` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aeceb0"></a> `00aeceb0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeceb4"></a> `00aeceb4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aeceb8"></a> `00aeceb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aecebc"></a> `00aecebc` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aecec0"></a> `00aecec0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecec4"></a> `00aecec4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecec8"></a> `00aecec8` | `81 66 44 f9` | ldr x1,[x20, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aececc"></a> `00aececc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeced0"></a> `00aeced0` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00aeced4"></a> `00aeced4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aeced8"></a> `00aeced8` | `9f 66 04 f9` | str xzr,[x20, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aecedc"></a> `00aecedc` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecee0"></a> `00aecee0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecee4"></a> `00aecee4` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aecee8"></a> `00aecee8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aece4c`](#insn-00aece4c) 範囲 `[['00aece4c', '00aece67']]`
  - `CONDITIONAL_JUMP` [`00aece64`](#insn-00aece64) → [`00aecedc`](#insn-00aecedc)
  - `FALL_THROUGH` [`00aece64`](#insn-00aece64) → [`00aece68`](#insn-00aece68)
- ブロック [`00aece68`](#insn-00aece68) 範囲 `[['00aece68', '00aece77']]`
  - `CONDITIONAL_JUMP` [`00aece74`](#insn-00aece74) → [`00aece8c`](#insn-00aece8c)
  - `FALL_THROUGH` [`00aece74`](#insn-00aece74) → [`00aece78`](#insn-00aece78)
- ブロック [`00aece78`](#insn-00aece78) 範囲 `[['00aece78', '00aece8b']]`
  - `FALL_THROUGH` [`00aece88`](#insn-00aece88) → [`00aece8c`](#insn-00aece8c)
- ブロック [`00aece8c`](#insn-00aece8c) 範囲 `[['00aece8c', '00aecea3']]`
  - `CONDITIONAL_JUMP` [`00aecea0`](#insn-00aecea0) → [`00aecec4`](#insn-00aecec4)
  - `FALL_THROUGH` [`00aecea0`](#insn-00aecea0) → [`00aecea4`](#insn-00aecea4)
- ブロック [`00aecea4`](#insn-00aecea4) 範囲 `[['00aecea4', '00aecec3']]`
  - `FALL_THROUGH` [`00aecec0`](#insn-00aecec0) → [`00aecec4`](#insn-00aecec4)
- ブロック [`00aecec4`](#insn-00aecec4) 範囲 `[['00aecec4', '00aecedb']]`
  - `FALL_THROUGH` [`00aeced8`](#insn-00aeced8) → [`00aecedc`](#insn-00aecedc)
- ブロック [`00aecedc`](#insn-00aecedc) 範囲 `[['00aecedc', '00aeceeb']]`

## 命令位置別の参照

- [`00aece4c`](#insn-00aece4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece50`](#insn-00aece50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece54`](#insn-00aece54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece60`](#insn-00aece60) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aece64`](#insn-00aece64) → [`00aecedc`](#insn-00aecedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece6c`](#insn-00aece6c) → `010a08d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aece74`](#insn-00aece74) → [`00aece8c`](#insn-00aece8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece88`](#insn-00aece88) → `010a08d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecea0`](#insn-00aecea0) → [`00aecec4`](#insn-00aecec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecec8`](#insn-00aecec8) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeced8`](#insn-00aeced8) → `010a08c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aecedc`](#insn-00aecedc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecee0`](#insn-00aecee0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aece4c`](#insn-00aece4c)

~~~json
{
  "source": "00aece4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece50`](#insn-00aece50)

~~~json
{
  "source": "00aece50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece54`](#insn-00aece54)

~~~json
{
  "source": "00aece54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece60`](#insn-00aece60)

~~~json
{
  "source": "00aece60",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aece64`](#insn-00aece64)

~~~json
{
  "source": "00aece64",
  "target": "00aecedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece6c`](#insn-00aece6c)

~~~json
{
  "source": "00aece6c",
  "target": "010a08d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aece74`](#insn-00aece74)

~~~json
{
  "source": "00aece74",
  "target": "00aece8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece88`](#insn-00aece88)

~~~json
{
  "source": "00aece88",
  "target": "010a08d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08d0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecea0`](#insn-00aecea0)

~~~json
{
  "source": "00aecea0",
  "target": "00aecec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecec8`](#insn-00aecec8)

~~~json
{
  "source": "00aecec8",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeced8`](#insn-00aeced8)

~~~json
{
  "source": "00aeced8",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aecedc`](#insn-00aecedc)

~~~json
{
  "source": "00aecedc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecee0`](#insn-00aecee0)

~~~json
{
  "source": "00aecee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
