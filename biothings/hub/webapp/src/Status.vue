<template>

    <div class="ui two column centered grid">
        <div class="four column centered row">
        </div>
        <div class="fourteen wide column centered row">
            <div class="column">
                <div class="ui statistics">
                    <div class="statistic">
                        <div class="value">
                            <i class="database icon"></i>
                            <span v-if="Object.keys(status).length && status.source && status.source.total">
                                <span v-if="status.source">{{status.source.total}}</span>
                                <span v-else></span>
                            </span>
                            <span v-else>0</span>
                        </div>
                        <div class="label">
                            <span v-if="Object.keys(status).length && status.source && status.source.total > 1">
                                Datasources
                            </span>
                            <span v-else>Datasource</span>
                        </div>
                    </div>
                    <div class="statistic">
                        <div class="text value">
                            <span v-if="Object.keys(status).length && status.source && status.source.documents">
                                <span v-if="status.source">
                                {{status.source.documents | formatNumber}}
                                </span>
                                <span v-else></span>
                            </span>
                            <span v-else>No</span>
                            <br>
                            <i class="file icon"></i>
                        </div>
                        <div class="label">
                            <span v-if="Object.keys(status).length && status.source && status.source.documents > 1">
                            Documents
                            </span>
                            <span v-else>Document (yet)</span>
                        </div>
                    </div>
                    <div class="statistic">
                        <div class="value">
                            <i class="cubes icon"></i>
                            <span v-if="Object.keys(status).length && status.build && status.build.total">
                                <span v-if="status.build">
                                    {{status.build.total}}
                                </span>
                                <span v-else></span>
                            </span>
                            <span v-else>0</span>
                        </div>
                        <div class="label">
                            <span v-if="Object.keys(status).length && status.build && status.build.total > 1">
                                Builds
                            </span>
                            <span v-else>Build</span>
                        </div>
                    </div>
                    <!--div class="statistic">
                    <div class="value">
                        <i class="ui shield alternate icon"></i>
                        <span v-if="status && status.api">
                            <span v-if="status.api.running && status.api.running > 0">
                                {{status.api.running}}/{{status.api.total}}
                            </span>
                            <span v-else>
                                {{status.api.total}}
                            </span>
                        </span>
                        <span v-else>??</span>
                    </div>
                    <div class="label">
                        <span v-if="status && status.api && status.api.running && status.api.running > 0">running </span>API
                    </div>
                    </div-->
                </div>
            </div>
        </div>


        <div class="four column centered row">
        </div>
        <div class="eight wide column centered row">
            <h4 class="ui blue header">What's new</h4>
            <div class="ui segment">
            <span v-if="Object.keys(whatsnew).length">
                <div class="column centered">

                    <div class="ui feed">
                        <div class="event" v-for="(newd,conf) in whatsnew">
                            <div class="label">
                                <i class="cubes icon"></i>
                            </div>
                            <div class="content">
                                <div class="summary">
                                    <a class="user">
                                        {{conf}}
                                    </a> can be rebuilt, it contains <a>{{Object.keys(newd.sources).length}} updated datasource(s)</a>.
                                    <br>
                                    <div class="date">
                                        Previous build was <i>{{ newd.old_build.name }}</i>, built on {{ newd.old_build.built_at | moment('lll') }}
                                    </div>
                                </div>
                                <div class="mymeta" v-for="(srcd,src) in newd.sources">
                                    <i class="database icon"></i><b>{{src}}</b>: {{srcd.old.version}} <i class="small arrow right icon"></i> {{srcd.new.version}}
                                    <i>({{srcd.new.downloaded_at | moment("from","now")}})</i>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
                <div class="four column centered row">
                </div>
            </span>
            <span v-else>Not much, nothing happened recently...</span>
            </div>


        </div>

    </div>
</template>

<script>
import Loader from './Loader.vue'
import axios from 'axios'
import bus from './bus.js'


export default {
  name: 'status',
  mixins: [ Loader, ],
  mounted () {
    console.log("Status mounted");
    this.refreshStatus();
    this.refreshWhatsNew();
  },
  created() {
  },
  beforeDestroy() {
  },
  data () {
      return  {
          status: {},
          whatsnew: {},
          errors: [],
      }
  },
  components: {Loader},
  methods: {
    refreshStatus: function() {
      this.loading();
      axios.get(axios.defaults.baseURL + '/status')
      .then(response => {
        this.status = response.data.result;
        this.loaded();
      })
      .catch(err => {
        console.log("Error getting sources information: " + err);
        this.loaderror(err)
      })
    },
    refreshWhatsNew: function() {
      axios.get(axios.defaults.baseURL + '/whatsnew')
      .then(response => {
        this.whatsnew = response.data.result;
      })
      .catch(err => {
        console.log("Error getting sources information: " + err);
      })
    },
  }
}
</script>

<style>
.mymeta { 
    color: rgba(0,0,0,.5);
    font-size: .85em;
}
</style>
