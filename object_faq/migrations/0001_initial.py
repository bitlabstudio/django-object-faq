# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EntryTranslation'
        db.create_table(u'object_faq_entry_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['object_faq.Entry'])),
        ))
        db.send_create_signal(u'object_faq', ['EntryTranslation'])

        # Adding unique constraint on 'EntryTranslation', fields ['language_code', 'master']
        db.create_unique(u'object_faq_entry_translation', ['language_code', 'master_id'])

        # Adding model 'Entry'
        db.create_table(u'object_faq_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'object_faq', ['Entry'])

        # Adding model 'GlobalObjectDescriptionTranslation'
        db.create_table(u'object_faq_globalobjectdescription_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['object_faq.GlobalObjectDescription'])),
        ))
        db.send_create_signal(u'object_faq', ['GlobalObjectDescriptionTranslation'])

        # Adding unique constraint on 'GlobalObjectDescriptionTranslation', fields ['language_code', 'master']
        db.create_unique(u'object_faq_globalobjectdescription_translation', ['language_code', 'master_id'])

        # Adding model 'GlobalObjectDescription'
        db.create_table(u'object_faq_globalobjectdescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'object_faq', ['GlobalObjectDescription'])


    def backwards(self, orm):
        # Removing unique constraint on 'GlobalObjectDescriptionTranslation', fields ['language_code', 'master']
        db.delete_unique(u'object_faq_globalobjectdescription_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'EntryTranslation', fields ['language_code', 'master']
        db.delete_unique(u'object_faq_entry_translation', ['language_code', 'master_id'])

        # Deleting model 'EntryTranslation'
        db.delete_table(u'object_faq_entry_translation')

        # Deleting model 'Entry'
        db.delete_table(u'object_faq_entry')

        # Deleting model 'GlobalObjectDescriptionTranslation'
        db.delete_table(u'object_faq_globalobjectdescription_translation')

        # Deleting model 'GlobalObjectDescription'
        db.delete_table(u'object_faq_globalobjectdescription')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'object_faq.entry': {
            'Meta': {'ordering': "['position']", 'object_name': 'Entry'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'object_faq.entrytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'EntryTranslation', 'db_table': "u'object_faq_entry_translation'"},
            'answer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['object_faq.Entry']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'object_faq.globalobjectdescription': {
            'Meta': {'object_name': 'GlobalObjectDescription'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'object_faq.globalobjectdescriptiontranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'GlobalObjectDescriptionTranslation', 'db_table': "u'object_faq_globalobjectdescription_translation'"},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['object_faq.GlobalObjectDescription']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['object_faq']
