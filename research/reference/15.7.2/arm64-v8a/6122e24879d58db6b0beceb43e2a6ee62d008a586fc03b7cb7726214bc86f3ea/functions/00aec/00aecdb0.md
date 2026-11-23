# 00aecdb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aece78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-af04985af54d07bec91bb2b6af96dcab)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecdb0",
  "name": "_ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b02a463b109e8015ae3dd39d941c2d277d213f831d8af3ea131e91ca27d8d5cc",
  "source_text_sha256": "b02a463b109e8015ae3dd39d941c2d277d213f831d8af3ea131e91ca27d8d5cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecdb0",
        "00aece4b"
      ]
    ],
    "bytes_sha256": "37daa4eddb4af5c72d1931c9b288c6dcfe4f81b0de123ca0e85bcffca501ecc3",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 601 bytes

~~~c

bool _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  char cVar1;
  bool bVar2;
  int iVar3;
  
  if (DAT_010a08d0 == '\0') {
    iVar3 = (**(code **)(*param_1 + 0x6b8))(param_1,DAT_010a08c8,param_2,param_3);
    cVar1 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar1 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    DAT_010a08d0 = iVar3 == 0;
    bVar2 = (bool)DAT_010a08d0;
  }
  else {
    bVar2 = false;
  }
  return bVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecdb0"></a> `00aecdb0` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aecdb4"></a> `00aecdb4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aecdb8"></a> `00aecdb8` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aecdbc"></a> `00aecdbc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aecdc0"></a> `00aecdc0` | `b5 2d 00 90` | adrp x21,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecdc4"></a> `00aecdc4` | `a8 42 63 39` | ldrb w8,[x21, #0x8d0] | `FALL_THROUGH`
<a id="insn-00aecdc8"></a> `00aecdc8` | `68 00 00 34` | cbz w8,0x00aecdd4 | `CONDITIONAL_JUMP`
<a id="insn-00aecdcc"></a> `00aecdcc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aecdd0"></a> `00aecdd0` | `1b 00 00 14` | b 0x00aece3c | `UNCONDITIONAL_JUMP`
<a id="insn-00aecdd4"></a> `00aecdd4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00aecdd8"></a> `00aecdd8` | `a9 2d 00 90` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aecddc"></a> `00aecddc` | `e3 03 02 aa` | mov x3,x2 | `FALL_THROUGH`
<a id="insn-00aecde0"></a> `00aecde0` | `e2 03 01 aa` | mov x2,x1 | `FALL_THROUGH`
<a id="insn-00aecde4"></a> `00aecde4` | `21 65 44 f9` | ldr x1,[x9, #0x8c8] | `FALL_THROUGH`
<a id="insn-00aecde8"></a> `00aecde8` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00aecdec"></a> `00aecdec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aecdf0"></a> `00aecdf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aecdf4"></a> `00aecdf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aecdf8"></a> `00aecdf8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aecdfc"></a> `00aecdfc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aece00"></a> `00aece00` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00aece04"></a> `00aece04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aece08"></a> `00aece08` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00aece0c"></a> `00aece0c` | `20 01 00 54` | b.eq 0x00aece30 | `CONDITIONAL_JUMP`
<a id="insn-00aece10"></a> `00aece10` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aece14"></a> `00aece14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aece18"></a> `00aece18` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00aece1c"></a> `00aece1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aece20"></a> `00aece20` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00aece24"></a> `00aece24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aece28"></a> `00aece28` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00aece2c"></a> `00aece2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aece30"></a> `00aece30` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00aece34"></a> `00aece34` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00aece38"></a> `00aece38` | `a0 42 23 39` | strb w0,[x21, #0x8d0] | `FALL_THROUGH`
<a id="insn-00aece3c"></a> `00aece3c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aece40"></a> `00aece40` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aece44"></a> `00aece44` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aece48"></a> `00aece48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecdb0`](#insn-00aecdb0) 範囲 `[['00aecdb0', '00aecdcb']]`
  - `CONDITIONAL_JUMP` [`00aecdc8`](#insn-00aecdc8) → [`00aecdd4`](#insn-00aecdd4)
  - `FALL_THROUGH` [`00aecdc8`](#insn-00aecdc8) → [`00aecdcc`](#insn-00aecdcc)
- ブロック [`00aecdcc`](#insn-00aecdcc) 範囲 `[['00aecdcc', '00aecdd3']]`
  - `UNCONDITIONAL_JUMP` [`00aecdd0`](#insn-00aecdd0) → [`00aece3c`](#insn-00aece3c)
- ブロック [`00aecdd4`](#insn-00aecdd4) 範囲 `[['00aecdd4', '00aece0f']]`
  - `CONDITIONAL_JUMP` [`00aece0c`](#insn-00aece0c) → [`00aece30`](#insn-00aece30)
  - `FALL_THROUGH` [`00aece0c`](#insn-00aece0c) → [`00aece10`](#insn-00aece10)
- ブロック [`00aece10`](#insn-00aece10) 範囲 `[['00aece10', '00aece2f']]`
  - `FALL_THROUGH` [`00aece2c`](#insn-00aece2c) → [`00aece30`](#insn-00aece30)
- ブロック [`00aece30`](#insn-00aece30) 範囲 `[['00aece30', '00aece3b']]`
  - `FALL_THROUGH` [`00aece38`](#insn-00aece38) → [`00aece3c`](#insn-00aece3c)
- ブロック [`00aece3c`](#insn-00aece3c) 範囲 `[['00aece3c', '00aece4b']]`

## 命令位置別の参照

- [`00aecdb0`](#insn-00aecdb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecdb4`](#insn-00aecdb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecdb8`](#insn-00aecdb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecdc4`](#insn-00aecdc4) → `010a08d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aecdc8`](#insn-00aecdc8) → [`00aecdd4`](#insn-00aecdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecdd0`](#insn-00aecdd0) → [`00aece3c`](#insn-00aece3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecde4`](#insn-00aecde4) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aece0c`](#insn-00aece0c) → [`00aece30`](#insn-00aece30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece38`](#insn-00aece38) → `010a08d0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aece3c`](#insn-00aece3c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aece40`](#insn-00aece40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecdb0`](#insn-00aecdb0)

~~~json
{
  "source": "00aecdb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecdb4`](#insn-00aecdb4)

~~~json
{
  "source": "00aecdb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecdb8`](#insn-00aecdb8)

~~~json
{
  "source": "00aecdb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecdc4`](#insn-00aecdc4)

~~~json
{
  "source": "00aecdc4",
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
- 参照命令 [`00aecdc8`](#insn-00aecdc8)

~~~json
{
  "source": "00aecdc8",
  "target": "00aecdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecdd0`](#insn-00aecdd0)

~~~json
{
  "source": "00aecdd0",
  "target": "00aece3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecde4`](#insn-00aecde4)

~~~json
{
  "source": "00aecde4",
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
- 参照命令 [`00aece0c`](#insn-00aece0c)

~~~json
{
  "source": "00aece0c",
  "target": "00aece30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece38`](#insn-00aece38)

~~~json
{
  "source": "00aece38",
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
- 参照命令 [`00aece3c`](#insn-00aece3c)

~~~json
{
  "source": "00aece3c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aece40`](#insn-00aece40)

~~~json
{
  "source": "00aece40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
